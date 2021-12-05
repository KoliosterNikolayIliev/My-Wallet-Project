from django.apps import AppConfig

from balance_caching_app.utils import AutoRequest

auto = AutoRequest


class BalanceCachingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'balance_caching_app'

    def ready(self):
        from balance_caching_app import scheduler
        scheduler.start()
        auto()
