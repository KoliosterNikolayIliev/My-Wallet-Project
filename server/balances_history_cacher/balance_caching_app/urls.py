import os

from django.urls import path

from balance_caching_app.mock_data_view import mock_data_view
from balance_caching_app.views import CreateBalance

mock = os.environ.get('USE_BALANCE_CACHE_MOCK')
if mock == 'True':
    urlpatterns = (
        path('add/', mock_data_view),
    )

else:
    urlpatterns = (
        path('add/', CreateBalance.as_view()),
    )
