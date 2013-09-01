from django.db import models
from hackerhane import settings

PAYMENT_MEDIA = (
         ("ELDEN", "Elden veya kutuya bıraktım"),
         ("BANKADAN-EFT", "EFT ile gönderdim"),
         ("BANKADAN-KREDI KARTI", "Kredi kartı ile gönderdim"),
     )


class BaseModelWithTimestamps(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    
    class Meta:
        abstract=True