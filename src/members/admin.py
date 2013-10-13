from django.contrib import admin
from members.models import HsUser, ExistingMemberInformation



admin.site.register(HsUser)

admin.site.register(ExistingMemberInformation)