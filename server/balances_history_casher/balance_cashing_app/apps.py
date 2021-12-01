from django.apps import AppConfig


class BalanceCashingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'balance_cashing_app'

    def ready(self):
        from balance_cashing_app import scheduler
        scheduler.start()
