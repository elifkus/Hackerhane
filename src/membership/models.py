from django.db import models
from hackerhane import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from accounting.models import EndOfDayBalance
from accounting.models import Transaction
from common.models import PAYMENT_MEDIA
    


class MembershipType(models.Model):
    name = models.CharField(max_length=32)
    monthly_fee_amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    
class Membership(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(MembershipType)
    custom_amount = models.DecimalField(max_digits=12, decimal_places=2)


class Payment(models.Model):
    MONTHS = (
        (1, 'Ocak'),
        (2, 'Şubat'),
        (3, 'Mart'),
        (4, 'Nisan'),
        (5, 'Mayıs'),
        (6, 'Haziran'),
        (7, 'Temmuz'),
        (8, 'Ağustos'),
        (9, 'Eylül'),
        (10, 'Ekim'),
        (11, 'Kasım'),
        (12, 'Aralık'),        
    )
        
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    paid_month = models.IntegerField(choices=MONTHS)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    for_membership = models.ForeignKey(Membership) 
    approved = models.BooleanField(default=False)
    media = models.CharField(choices=PAYMENT_MEDIA, max_length=32) 
    
    __approved = None
    
    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        self.__approved = self.approved

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.approved and self.approved != self.__approved:
            raise ValidationError("An approved payment cannot be changed")

        super(Payment, self).save(force_insert, force_update, *args, **kwargs)
        self.__approved = self.approved


#generate transaction when payment is approved
@receiver(post_save, sender=Payment)
def insert_transaction_for_payment(sender, instance, **kwargs):
    if instance.approved:
        note =  instance.get_month_display() + " ayı aidatı - " + " ".join(instance.for_membership.users) 
        transaction = Transaction(amount=instance.amount, realized_date=instance.payment_date,
                                  created_by=instance.updated_by, updated_by=instance.updated_by,
                                  note=note, type_id=1, media=instance.media)
        
        transaction.save()
        