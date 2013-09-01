from django.contrib import admin
from accounting.models import  Transaction, TransactionType, MonthlyRecurringExpense
from common.admin import BaseModelWithTimestampsAdmin


class TransactionAdmin(BaseModelWithTimestampsAdmin):
    list_display = ['realized_date', 'amount', 'type', 'note', 'payment_media',]
    ordering = ['-realized_date',]
    
admin.site.register(Transaction, TransactionAdmin)

admin.site.register(TransactionType)

class MonthlyRecurringExpenseAdmin(admin.ModelAdmin):
    list_display = ['type', 'amount_with_currency', 'day_of_occurrence',]
    

admin.site.register(MonthlyRecurringExpense, MonthlyRecurringExpenseAdmin)
