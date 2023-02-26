from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password,  **extra_fields):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

class Nomenclature(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    selling_price = models.DecimalField(max_digits=9, decimal_places=2)
    rec_purchase_price = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_quantity = models.DecimalField(max_digits=9, decimal_places=2)
    in_stock_quantity = models.DecimalField(max_digits=9, decimal_places=2) 