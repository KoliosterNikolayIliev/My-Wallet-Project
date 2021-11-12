from django.urls import path
from monitor_app.views import index_view
from django.contrib.auth.views import LoginView, LogoutView
from django_otp.forms import OTPAuthenticationForm
from monitor_app.views import Register, TOTPCreateView

urlpatterns = [
    path('', index_view, name="index"),
    path('accounts/login/', LoginView.as_view(authentication_form=OTPAuthenticationForm), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', Register.as_view(), name='register'),
    path('accounts/barcode/<username>', TOTPCreateView.as_view(), name='barcode')

]
