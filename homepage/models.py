from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

#Create users model
class User(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=300, null=True)
    TTL = models.DateField(null=True)
    blood_pressure = models.CharField(max_length=100, null=True)
    weight = models.CharField(max_length=100, null=True)
    vein = models.CharField(max_length=100, null=True)
    temp = models.CharField(max_length=100, null=True)
    drink_perday = models.CharField(max_length=100,null=True)
    food = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username