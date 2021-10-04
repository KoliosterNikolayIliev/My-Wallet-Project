from django.contrib import admin

from authentication.models import UserProfile


class User_tets(admin.AllValuesFieldListFilter):
    model = UserProfile


admin.site.register(UserProfile)


# class ArtAdmin(admin.ModelAdmin):
#     list_display = ('id', 'type', 'name', 'date_created')
#     list_filter = ('type', 'id', 'date_created')
#     inlines = (
#         LikeInline,
#     )
#
#
# admin.site.register(Item, ArtAdmin)
# admin.site.register(Comment)
# admin.site.register(Like)
