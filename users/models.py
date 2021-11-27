from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from patients.models import PatientsInfo


class CustomAccountManager(BaseUserManager):

    def create_user(self,
                    email: str,
                    username: str,
                    password: str,
                    **other_fields) -> object:
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        other_fields.setdefault('is_active', True)
        user = self.model(
            email=email,
            username=username,
            **other_fields)
        user.set_password(password)
        user.save()
        return user
        # return self.create_user(email, username, password, **other_fields)

    def create_superuser(self,
                         email: str,
                         username: str,
                         password: str,
                         **other_fields) -> object:
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True.'))

        if other_fields.get('is_active') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_active=True.'))

        return self.create_user(email, username, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateField(
        verbose_name='date joined',
        auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)

    role = models.CharField(max_length=100, default='醫師')
    photo_url = models.URLField(max_length=200, default='')

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
