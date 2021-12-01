from django.urls import path

from balance_cashing_app.views import GetBalances, CreateBalance

urlpatterns = (
    path('', GetBalances.as_view()),
    path('add/', CreateBalance.as_view()),
)
