from djongo import models

from encrypted_model_fields.fields import EncryptedCharField


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    user_identifier = models.CharField(max_length=40, blank=False)
    base_currency = models.CharField(max_length=5, default='GBP')
    source_label = models.CharField(max_length=20, blank=True)

    # Binance access
    binance_key = EncryptedCharField(max_length=200, blank=True)
    binance_secret = EncryptedCharField(max_length=200, blank=True)

    # Coinbase access
    coinbase_api_secret = EncryptedCharField(max_length=200, blank=True)
    coinbase_api_key = EncryptedCharField(max_length=200, blank=True)


class NordigenRequisition(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    institution_id = models.CharField(max_length=100)
    requisition_id = EncryptedCharField(max_length=100)
    confirmation_link = EncryptedCharField(max_length=300)
