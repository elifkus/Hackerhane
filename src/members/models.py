from django.db import models
from hackerhane import settings

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group, PermissionsMixin)
from django.core.urlresolvers import reverse
from membership.models import Membership
import logging


logger = logging.getLogger(__name__)


class HsUserManager(BaseUserManager):
    def create_user(self, email, cell_phone_number, is_student, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        full_name = kwargs.get("full_name", None)
        is_active = kwargs.get("is_active", False)
        
        user = self.model(
            email=self.normalize_email(email),
            cell_phone_number=cell_phone_number,
            is_student=is_student, full_name=full_name, 
            is_active=is_active
        )
        
        add_to_member_group(user)
        
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user


    def create_superuser(self, email, cell_phone_number, is_student, password, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        full_name = kwargs.get("full_name", None)

        user = self.create_user(email,
            cell_phone_number=cell_phone_number,
            is_student=is_student,
            password=password,
            full_name=full_name
        )
        user.is_admin = True
        user.is_active = False
        
        full_name = kwargs.get("full_name", None)
        
        user.full_name = full_name
                
        user.save(using=self._db)
        return user


def add_to_member_group(user):
    if check_if_existing_hackerspace_member(user.email):
        group = Group.objects.get(name="Member")
        user.groups.add(group)

def check_if_existing_hackerspace_member(email):
    exists = False
    
    try:
        ExistingMemberInformation.objects.get(email=email)
        exists =  True
    except ExistingMemberInformation.DoesNotExist:
        logger.info("User with email address %s could not be found" % email)
        pass
    return exists

class HsUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='eposta adresi',
        max_length=255,
        unique=True,
        db_index=True,
    )
    full_name = models.CharField('isim soyisim',max_length=64)
    email_visible = models.BooleanField('epostamı başkaları görebilsin mi?', default=False)
    nickname = models.CharField('nick', max_length=32, blank=True, null=True)
    cell_phone_number = models.CharField('cep numarası', max_length=16)
    cell_phone_number_visible = models.BooleanField('telefon numaramı başkaları görebilsin mi?', default=False)
    is_student = models.BooleanField('öğrenci miyim?', default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    summary = models.TextField('ben kimim ne yaparım?', blank=True, null=True)
    reason = models.TextField('hackerspace çünkü', blank=True, null=True)
    
    
    objects = HsUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cell_phone_number', 'is_student', 'full_name']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.nickname

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def get_absolute_url(self):
        return reverse('show-member', kwargs={'pk': self.pk})
    @property
    def is_staff(self):
        return self.is_admin

    
class WebLink(models.Model):
    WEB_SITES = (
        ('LINKEDIN', 'linkedin'),
        ('FACEBOOK', 'facebook'),
        ('GOOGLE+', 'google+'),
        ('GITHUB', 'github'),
        ('HOMEPAGE', 'kişisel')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.CharField(max_length=16, choices=WEB_SITES)
    link = models.URLField()
    

class ExistingMemberInformation(models.Model):    
    email = models.EmailField(
        verbose_name='eposta adresi',
        max_length=255,
        unique=True,
        db_index=True,
    )
    full_name = models.CharField('isim soyisim',max_length=64)
    cell_phone_number = models.CharField('cep numarası', max_length=16)
    is_student = models.BooleanField('öğrenci miyim?', default=False)
    is_active = models.BooleanField(default=True)
    member_since_date = models.DateField()
    memberships = models.ManyToManyField(Membership, null=True, blank=True) 

    