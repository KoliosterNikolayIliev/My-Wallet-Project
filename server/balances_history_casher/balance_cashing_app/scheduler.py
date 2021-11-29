import time

from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from balance_cashing_app.models import UserData
from balance_cashing_app.views import _auto_create_balance


def update_balances():
    start_time = time.time()
    # users is just for testing
    users = UserData.objects.all()
    for user in users:
        # user balance will come from portfolio async function
        data = {
            'id': user.user_identifier,
            'balance': 700,
            'timestamp': timezone.now()
        }
        _auto_create_balance(data)

    end_time = time.time()
    measured_time = end_time - start_time
    print(measured_time)
    return measured_time


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_balances, 'interval', minutes=0.1)
    scheduler.start()
