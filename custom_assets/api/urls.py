from django.urls import path

from api.views import CreateCryptoAsset, GetAssets

urlpatterns = (
    path('', GetAssets.as_view()),
    path('crypto/', CreateCryptoAsset.as_view()),
)
