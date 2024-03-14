from django.db import models

# Create your models here.

class Message(models.Model):
    #Set user id as primary key
    user_id = models.CharField(max_length=1000, primary_key=True)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_id