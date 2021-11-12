import os
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from pymongo import MongoClient


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(
        host=host,
        port=int(port),
        username=username,
        password=password
    )
    return client[db_name]


def get_number_of_users():
    db_name = '3vial'
    db_host = os.environ.get('DB_HOST')
    db_port = 27017
    db_username = os.environ.get('DB_USERNAME').strip()
    db_password = os.environ.get('DB_PASSWORD').strip()

    db = get_db_handle(
        db_name,
        db_host,
        db_port,
        db_username,
        db_password)
    collection = db['authentication_userprofile']
    return collection.estimated_document_count()


def get_assets():
    return 15000


def get_user_totp_device(self, user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device