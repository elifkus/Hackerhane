from django.db import models
from hackerhane import settings

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class HsUserManager(BaseUserManager):
    def create_user(self, email, cell_phone_number, is_student, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            cell_phone_number=cell_phone_number,
            is_student=is_student
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cell_phone_number, is_student, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            cell_phone_number=cell_phone_number,
            is_student=is_student,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class HsUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='eposta adresi',
        max_length=255,
        unique=True,
        db_index=True,
    )
    full_name = models.CharField(max_length=64)
    email_visible = models.BooleanField('epostamı başkaları görebilsin mi?', default=False)
    nickname = models.CharField(max_length=32,blank=True, null=True)
    cell_phone_number = models.CharField(max_length=16)
    cell_phone_number_visible = models.BooleanField('telefonumu numaramı başkaları görebilsin mi?', default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    summary = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
 
    objects = HsUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cell_phone_number', 'is_student']

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
    

    
    

    