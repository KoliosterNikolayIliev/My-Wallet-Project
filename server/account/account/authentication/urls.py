from django.urls import path

from authentication.views.create_delete_nordigen_requisition import CreateDeleteNordigenRequisition
from authentication.views.get_put_delete_view import get_put_create_delete_user_profile
from authentication.views.nordigen_banks import get_nordigen_banks
from authentication.views.yodlee_token import get_yodlee_token

urlpatterns = [
    path('user', get_put_create_delete_user_profile),
    path('internal/user', get_put_create_delete_user_profile),
    path('user/bank', CreateDeleteNordigenRequisition.as_view()),
    path('user/yodlee-token', get_yodlee_token),
    path('user/nordigen-banks', get_nordigen_banks)
]
