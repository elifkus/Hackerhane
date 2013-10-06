from django.db import models
from datetime import timedelta
from common.models import PAYMENT_MEDIA
from common.models import BaseModelWithTimestamps


class TransactionType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    
class Transaction(BaseModelWithTimestamps):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    realized_date = models.DateField()
    note = models.CharField(max_length=256)
    type = models.ForeignKey(TransactionType)
    payment_media = models.CharField(max_length=32, choices=PAYMENT_MEDIA)
       
    def type_str(self):
        return str(self.type)
    
             
    def balance(self):
        day_before = self.date - timedelta(days=1)      
        end_of_day = EndOfDayBalance.objects.filter(date=day_before)
        
        if end_of_day:
            end_of_day_balance = end_of_day.amount
            transactions = Transaction.objects.filter(date=self.date, created_time__is_lt=True)
        else:
            end_of_day_balance = 0
            transactions = Transaction.objects.all()
            
        amount_list = transactions.values_list('amount', flat=True)
        
        return end_of_day_balance + sum(amount_list)
    
        
class EndOfDayBalance(models.Model):
    date = models.DateField()
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    
    
class ExpectedIncome(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=256)
    type = models.ForeignKey(TransactionType)
    expected_date = models.DateField()
    
    
class ExpectedExpense(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=256)
    type = models.ForeignKey(TransactionType)
    expected_date = models.DateField()
    

class MonthlyRecurringExpense(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.ForeignKey(TransactionType)
    day_of_occurrence = models.IntegerField()
    
    def amount_with_currency(self):
        #TODO: Fix how it is shown
        return "%d TL" % self.amount
    
    