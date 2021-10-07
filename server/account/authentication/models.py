from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile(models.Model):
    user_identifier = models.CharField(max_length=40, blank=False)
    base_currency = models.CharField(max_length=20, default='GBP')
    source_label = models.CharField(max_length=20, blank=True)
    # All of these will be encrypted fields (https://pypi.org/project/django-encrypted-model-fields/)
    # The rest will be added in future
    binance_key = models.CharField(max_length=100, blank=True, )
    binance_secret = models.CharField(max_length=100, blank=True)
    yodlee_login_name = models.CharField(max_length=180, blank=True)
