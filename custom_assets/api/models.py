from djongo import models


# Create your models here.

class CryptoAsset(models.Model):
    type = models.CharField(max_length=5)
    amount = models.FloatField()

    class Meta:
        abstract = True


class StockAsset(models.Model):
    type = models.CharField(max_length=5)
    amount = models.IntegerField()

    class Meta:
        abstract = True


class CurrencyAsset(models.Model):
    type = models.CharField(max_length=3)
    amount = models.FloatField()

    class Meta:
        abstract = True


class UserAssets(models.Model):
    user_key = models.CharField(
        max_length=50,
    )

    crypto_assets = models.ArrayField(
        model_container=CryptoAsset,
    )

    stock_assets = models.ArrayField(
        model_container=StockAsset,
    )

    currency_assets = models.ArrayField(
        model_container=CurrencyAsset,
    )
