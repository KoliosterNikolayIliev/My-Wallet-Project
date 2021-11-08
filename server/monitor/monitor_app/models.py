from django.db import models


class Monitor(models.Model):
    number_of_accounts = models.IntegerField(default=0)
    total_assets_on_platform = models.FloatField(default=0)
