from django.urls import path
from authentication.views.get_put_delete_view import get_put_create_delete_user_profile

urlpatterns = [
    path('user', get_put_create_delete_user_profile),
    path('user/edit', get_put_create_delete_user_profile),
    path('user/delete', get_put_create_delete_user_profile),
    path('internal/user', get_put_create_delete_user_profile),

]
