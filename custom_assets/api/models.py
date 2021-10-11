from django.db import models


# Create your models here.

class CryptoAsset(models.Model):
    custom_assets_key = models.CharField(max_length=50)
    crypto = models.CharField(max_length=5)
    amount = models.FloatField()
