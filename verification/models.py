from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=20,blank=True)
    national_code = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='Profile',blank=True ,null=True)


    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
