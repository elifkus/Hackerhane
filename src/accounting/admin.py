from django.contrib import admin
from accounting.models import  Transaction, TransactionType, TransactionMedia



admin.site.register(Transaction)

admin.site.register(TransactionType)

admin.site.register(TransactionMedia)