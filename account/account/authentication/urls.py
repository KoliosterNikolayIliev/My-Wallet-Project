from django.urls import path

from authentication.views.create_delete_nordigen_requisition import CreateDeleteNordigenRequisition
from authentication.views.get_put_delete_view import get_put_create_delete_user_profile

urlpatterns = [
    path('user', get_put_create_delete_user_profile),
    path('internal/user', get_put_create_delete_user_profile),
    path('user/bank', CreateDeleteNordigenRequisition.as_view()),
]
