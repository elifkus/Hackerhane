from django.contrib import admin
from members.models import HsUser, ExistingMemberInformation, WebLink



admin.site.register(HsUser)

admin.site.register(ExistingMemberInformation)

admin.site.register(WebLink)