import os
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from pymongo import MongoClient


client = MongoClient(host=os.environ.get('DB_HOST'))


def get_number_of_users():
    db = client['3vial']
    collection = db['authentication_userprofile']
    return collection.estimated_document_count()


def get_assets():
    return 15000


def get_user_totp_device(self, user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device
