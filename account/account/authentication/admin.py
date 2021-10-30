from django.contrib import admin

from authentication.models import UserProfile, NordigenRequisition


class AdminUserProfile(admin.AllValuesFieldListFilter):
    model = UserProfile


class AdminNordigenRequisition(admin.AllValuesFieldListFilter):
    model = NordigenRequisition


admin.site.register(UserProfile)
admin.site.register(NordigenRequisition)
