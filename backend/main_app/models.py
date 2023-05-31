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

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField(null=True)
    name = models.CharField(max_length=256, null=True)
    wholesale_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    purchase_quantity = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Nomenclature(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True)
    selling_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024, null=True)
    date_create = models.DateField(auto_created=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Provider_Requisits(models.Model):
    id = models.AutoField(primary_key=True)
    inn = models.IntegerField(null=True)
    ogrn = models.IntegerField(null=True)
    address = models.CharField(max_length=2048, null=True)
    provider_id = models.IntegerField(null=True)
    org_type = models.CharField(max_length=256, null=True)
    bank_name = models.CharField(max_length=512, null=True)
    bank_account = models.BigIntegerField(null=True)
    bank_bik = models.IntegerField(null=True)
    bank_cors_account = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Provider_x_Nomenclature(models.Model):
    nomenclature_id = models.IntegerField(null=True)
    provider_id = models.IntegerField(null=True)
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=128, null=True)
    email = models.EmailField(max_length=40, null=True)
    birthday_date = models.DateField(null=True)
    description = models.CharField(max_length=1024, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Provider_x_Contact(models.Model):
    contact_id = models.IntegerField(null=True)
    provider_id = models.IntegerField(null=True)
