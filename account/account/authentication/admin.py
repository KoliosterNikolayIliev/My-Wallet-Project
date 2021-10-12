from django.contrib import admin

from authentication.models import UserProfile


class AdminUserProfile(admin.AllValuesFieldListFilter):
    model = UserProfile


admin.site.register(UserProfile)
