from djongo import models


class Source(models.Model):
    provider = models.CharField(max_length=50, primary_key=True)
    value = models.FloatField()

    class Meta:
        managed = False


class Balance(models.Model):
    balance = models.FloatField(primary_key=True)
    source_balances = models.ArrayField(
        model_container=Source
    )
    timestamp = models.DateTimeField()

    class Meta:
        managed = False


class UserData(models.Model):
    user_identifier = models.CharField(max_length=500)
    last_login = models.DateTimeField()
    balances_history = models.ArrayField(
        model_container=Balance
    )
