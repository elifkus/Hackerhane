from django.contrib import admin
from membership.models import MembershipType, Membership, FeePayment
from common.admin import BaseModelWithTimestampsAdmin


class FeePaymentAdmin(BaseModelWithTimestampsAdmin):
    pass


admin.site.register(MembershipType)

admin.site.register(Membership)

admin.site.register(FeePayment, FeePaymentAdmin)