from django.contrib.auth.models import AbstractUser, User
from django.db import models

from encrypted_model_fields.fields import EncryptedCharField


class UserProfile(models.Model):

    user_identifier = models.CharField(max_length=40, blank=False)
    base_currency = models.CharField(max_length=20, default='GBP')
    source_label = models.CharField(max_length=20, blank=True)
    # All of these will be encrypted fields (https://pypi.org/project/django-encrypted-model-fields/)
    # The rest will be added in future
    binance_key = EncryptedCharField(max_length=500, blank=True)
    binance_secret = EncryptedCharField(max_length=500, blank=True)
    yodlee_login_name = EncryptedCharField(max_length=500, blank=True)
    nordigen_requisition = EncryptedCharField(max_length=500, blank=True)
