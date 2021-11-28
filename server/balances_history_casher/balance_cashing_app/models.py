from djongo import models


class Balance(models.Model):
    balance = models.FloatField(primary_key=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False


class UserData(models.Model):
    user_identifier = models.CharField(max_length=500, )
    last_login = models.DateTimeField()
    balances_history = models.ArrayField(
        model_container=Balance
    )
