from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    class meta:
        verbose_name = 'auth_user'
        verbose_plural = 'auth_users'
        db_table = 'auth_user'



