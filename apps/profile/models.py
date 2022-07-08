from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=30, validators=(
        RegexValidator(r'^([A-Z]{1}[a-z]{1,19})$',
                       'Name must start with the capital letter and contain from 2 to 20 letters. Example: Andriy'),
    ))
    surname = models.CharField(max_length=30, validators=(
        RegexValidator(r'^([A-Z]{1}[a-z]{1,19})$',
                       'Surname must start with the capital letter and contain from 2 to 20 letters. Example: Popov'),
    ))
    born = models.DateField()
    phone = models.CharField(max_length=13, validators=(
        RegexValidator(r'^\+380[\d]{9}$', 'Invalid phone number. Example: +380xxxxxxxxx'),
    ))
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')