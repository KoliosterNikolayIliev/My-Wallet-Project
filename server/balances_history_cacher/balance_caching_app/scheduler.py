import os
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from balance_caching_app.models import UserData
from balance_caching_app.utils import user_is_not_active, AutoRequest


def update_balances():
    users = UserData.objects.all()
    for user in users:
        AutoRequest.auto = True
        sleep_time = os.environ.get('AUTO_UPDATE_USER_DELAY')
        time.sleep(float(sleep_time))
        if user_is_not_active(user.last_login):
            continue
        user_id = user.user_identifier
        headers = {'Authorization': user_id}
        url = os.environ.get('AUTO_CACHING_URL')
        try:
            requests.get(url + 'api/assets', headers=headers)
        except Exception as e:
            print('Connection to porfolio cashing service failed:' + str(e))
            break
    AutoRequest.auto = False


def start():
    scheduler = BackgroundScheduler()
    update_interval = float(os.environ.get('DB_AUTO_CACHING_INTERVAL'))
    scheduler.add_job(update_balances, 'interval', minutes=update_interval)
    scheduler.start()
