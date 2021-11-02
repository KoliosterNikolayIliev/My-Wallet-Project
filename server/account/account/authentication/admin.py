from django.contrib import admin

from authentication.models import UserProfile, NordigenRequisition


class AdminNordigenRequisition(admin.TabularInline):
    model = NordigenRequisition


class SiteAdmin(admin.ModelAdmin):
    inlines = (
        AdminNordigenRequisition,
    )


admin.site.register(UserProfile, SiteAdmin)


