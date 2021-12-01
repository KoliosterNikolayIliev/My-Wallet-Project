from django.apps import AppConfig


class BalanceCachingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'balance_caching_app'

    def ready(self):
        from balance_caching_app import scheduler
        scheduler.start()
