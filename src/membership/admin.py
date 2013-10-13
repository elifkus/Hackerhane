from django.contrib import admin
from membership.models import MembershipType, Membership

admin.site.register(MembershipType)

admin.site.register(Membership)
