import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin

from django.db import models

from .managers import UserManager

# Create your models here.


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{ self.email }: {self.first_name} { self.last_login } ({ self.username })"



