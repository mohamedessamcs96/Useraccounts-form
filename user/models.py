from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,
                            on_delete=models.CASCADE)
    age=models.IntegerField()



def __str__(self):
    return self.user.username
