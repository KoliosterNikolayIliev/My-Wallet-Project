import os
import time

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from balance_caching_app.models import UserData
from balance_caching_app.views import _auto_create_balance


def update_balances():
    start_time = time.time()

    users = UserData.objects.all()
    for user in users:
        # time.sleep(300)
        user_id = user.user_identifier
        headers = {'Authorization': user_id}
        url = os.environ.get('AUTO_CACHING_URL')
        response = requests.get(url + 'api/assets', headers=headers)
        total_balance = response.json()['total']
        data = {
            'id': user.user_identifier,
            'balance': total_balance,
            'timestamp': timezone.now()
        }
        _auto_create_balance(data)

    end_time = time.time()
    measured_time = end_time - start_time
    return measured_time


def start():
    scheduler = BackgroundScheduler()
    update_interval = int(os.environ.get('DB_AUTO_CACHING_INTERVAL'))
    scheduler.add_job(update_balances, 'interval', minutes=update_interval)
    scheduler.start()