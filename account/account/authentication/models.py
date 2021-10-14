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
    coinbase_api_pass = EncryptedCharField(max_length=200, blank=True)

    # Yodlee access
    yodlee_login_name = EncryptedCharField(max_length=150, blank=True)

    # Nordigen access
    nordigen_requisition = EncryptedCharField(max_length=200, blank=True)
    # Custom Assets
    custom_assets_key = EncryptedCharField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        self.nordigen_requisition = str(self.id) + self.user_identifier
        self.yodlee_login_name = self.user_identifier + str(self.id)
        self.custom_assets_key = str(self.id) + self.user_identifier + str(self.id)
        super(UserProfile, self).save(*args, **kwargs)
