from django.urls import path

from api.views import CreateCryptoAsset

urlpatterns = (
    path('crypto/', CreateCryptoAsset.as_view()),
)
