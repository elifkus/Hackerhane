from django.db import models
from hackerhane import settings
from django.core.exceptions import ValidationError
from accounting.models import Transaction
from common.models import PAYMENT_MEDIA, BaseModelWithTimestamps
from common.utils import  note_from_month_index


class MembershipType(models.Model):
    name = models.CharField(max_length=32)
    monthly_fee_amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.name

    
class Membership(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(MembershipType)
    custom_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        users_str = [str(user) for user in self.users.all()]
        
        if not users_str:
            users_str = ''
        else:
            users_str = "~".join(users_str)
            
        return "%s - %s" % (users_str, self.type)

class FeePayment(BaseModelWithTimestamps):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    paid_month = models.DateField()
    for_membership = models.ForeignKey(Membership) 
    approved = models.BooleanField(default=False)
    media = models.CharField(choices=PAYMENT_MEDIA, max_length=32) 
    transactions = models.ManyToManyField(Transaction, null=True, blank=True, related_name='+')
    
    __approved = None
    
    def __str__(self):
        return "%d TL - %s - Approved %s" % (self.amount, str(self.payment_date), str(self.approved))
    
    def __init__(self, *args, **kwargs):
        super(FeePayment, self).__init__(*args, **kwargs)
        self.__approved = self.approved

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.id and self.approved and (self.approved != self.__approved):
            raise ValidationError("An approved payment cannot be changed")

        super(FeePayment, self).save(force_insert, force_update, *args, **kwargs)
        
        if self.approved:
            transaction = insert_transaction_for_payment(self)
            #add to current object
            self.transactions.add(transaction)
            super(FeePayment, self).save(force_insert, force_update, *args, **kwargs)
        
        self.__approved = self.approved


def insert_transaction_for_payment(instance):
    note = note_from_month_index(instance.paid_month.month, instance.for_membership)
    transaction = Transaction(amount=instance.amount, realized_date=instance.payment_date,
                              created_by=instance.updated_by, updated_by=instance.updated_by,
                              note=note, type_id=1, payment_media=instance.media)
    transaction.save()
    
    return transaction
    