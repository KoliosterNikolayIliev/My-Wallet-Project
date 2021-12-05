from django.urls import path

from balance_caching_app.views import CreateBalance

urlpatterns = (
    # path('', GetBalances.as_view()),
    path('add/', CreateBalance.as_view()),
)
