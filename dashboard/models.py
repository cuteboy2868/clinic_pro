from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    full_name = models.CharField(max_length=55, db_index=True)
    address = models.CharField(max_length=75, null=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[/+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid number',
        )])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'User'


class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    status = models.IntegerField(default=5, choices=
        (1, 'doctor')
        (2, 'manager')
        )

