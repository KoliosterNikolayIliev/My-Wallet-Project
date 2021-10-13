from django.urls import path

from api.views import CreateCryptoAsset, GetAssets, CreateStockAsset

urlpatterns = (
    path('', GetAssets.as_view()),
    path('crypto/', CreateCryptoAsset.as_view()),
    path('stock/', CreateStockAsset.as_view()),
)
