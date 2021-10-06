from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile(models.Model):
    user_identifier = models.CharField(max_length=30, blank=False)
    base_currency = models.CharField(max_length=20, default='GBP')
    source_label = models.CharField(max_length=20, default='Not set!')
    # All of these will be encrypted fields (https://pypi.org/project/django-encrypted-model-fields/)
    # The rest will be added in future
    binance_key = models.CharField(max_length=100, blank=False, default='Not set!')
    binance_secret = models.CharField(max_length=100, blank=False, default='Not set!')
    yodlee_login_name = models.CharField(max_length=20, blank=False, default='Not set!')

    # Unsuccessful attempt to add id due to id length
    # def save(self, *args, **kwargs):
    #     ascii_values = [str(ord(character)) for character in self.user_identifier]
    #     self.id = int(''.join(ascii_values))
    #     return super(UserProfile, self).save(*args, **kwargs)
