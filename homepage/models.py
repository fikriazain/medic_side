from django.db import models

# Create your models here.

#Create users model
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username