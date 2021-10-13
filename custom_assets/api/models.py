from djongo import models


# Create your models here.

class CryptoAsset(models.Model):
    type = models.CharField(max_length=5)
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
