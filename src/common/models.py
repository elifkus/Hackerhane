from django.db import models
from hackerhane import settings

PAYMENT_MEDIA = (
         ("ELDEN", "Elden verdim / Elden verdim"),
         ("KUTU", "Kutuya bıraktım / Kutudan aldım"),
         ("BANKADAN-EFT", "EFT ile gönderdim"),
         ("BANKADAN-KREDI KARTI", "Kredi kartı ile gönderdim"),
     )

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


class BaseModelWithTimestamps(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='+')
    
    class Meta:
        abstract=True