from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

#Users
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, phone, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, phone, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, phone, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name,  last_name=last_name, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Profile(AbstractBaseUser, PermissionsMixin):

    STATE = (
    ('Student', 'Student'),
    ('Professional', 'Professional'),
    )

    email = models.EmailField(_('email address'), unique=True, default="")
    user_name = models.CharField(max_length=150, unique=True, default="")
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    DOB = models.DateField(default=timezone.now)
    university = models.CharField(max_length=50000,blank=True,null=True)
    branch = models.CharField(max_length=50000,blank=True,null=True)
    specitalization = models.CharField(max_length=50000,blank=True,null=True)
    bio = models.TextField(max_length=50000,blank=True,null=True)
    status = models.CharField(max_length=100,choices=STATE,null=True)
    endyear = models.IntegerField(blank=True,null=True)
    phone = PhoneNumberField(blank=False, unique=True)
    point = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'phone']
