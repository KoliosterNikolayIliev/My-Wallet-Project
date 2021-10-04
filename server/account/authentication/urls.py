from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.public),
    path('private/', views.private)
]