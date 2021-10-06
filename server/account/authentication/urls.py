from django.urls import path

from authentication.views.delete_profile_view import delete_user_account
from authentication.views.get_and_create_view import get_and_create_user_profile

urlpatterns = [
    path('user/', get_and_create_user_profile, name="user_details"),
    path('user/edit', delete_user_account, name="delete_user"),
    path('user/delete', delete_user_account, name="delete_user"),
]
