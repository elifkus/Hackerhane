from django.contrib import admin
from members.models import HsUser


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(HsUser, UserAdmin)