from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128, validators=(
        RegexValidator(
            r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
            'Password must contain at least 8 characters: 1 num, 1 uppercase letter, 1 lowercase letter, '
            '1 non-alpha-numeric '
        ),
    ))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()