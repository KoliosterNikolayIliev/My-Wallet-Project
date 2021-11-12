from django.urls import path
from monitor_app.views import index_view, register_user
from django.contrib.auth.views import LoginView, LogoutView
from django_otp.forms import OTPAuthenticationForm


urlpatterns = [
    path('', index_view, name="index"),
    path('accounts/login/', LoginView.as_view(authentication_form=OTPAuthenticationForm), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', register_user, name='register'),
]
