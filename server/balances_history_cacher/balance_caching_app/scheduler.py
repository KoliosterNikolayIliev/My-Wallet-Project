import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from balance_caching_app.models import UserData
from balance_caching_app.utils import user_is_not_active
from balance_caching_app.views import _auto_create_balance


def update_balances():
    users = UserData.objects.all()
    for user in users:
        # time.sleep(300)
        if user_is_not_active(user.last_login):
            continue
        user_id = user.user_identifier
        headers = {'Authorization': user_id}
        url = os.environ.get('AUTO_CACHING_URL')
        try:
            response = requests.get(url + 'api/assets', headers=headers)
        except Exception as e:
            print('Connection to porfolio cashing service failed:' + str(e))
            break
        total_balance = response.json()['total']
        data = {
            'id': user.user_identifier,
            'balance': total_balance,
            'timestamp': timezone.now()
        }
        _auto_create_balance(data)


def start():
    scheduler = BackgroundScheduler()
    update_interval = float(os.environ.get('DB_AUTO_CACHING_INTERVAL'))
    scheduler.add_job(update_balances, 'interval', minutes=update_interval)
    scheduler.start()
