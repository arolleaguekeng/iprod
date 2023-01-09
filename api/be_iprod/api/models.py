from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15,null=False)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=25,null=False)

    class Meta:
        verbose_name = "User"


class Creation(models.Model):
    name = models.CharField(max_length=100, null=False, default="default")
    image = models.TextField(null=False)
    descriptions = models.CharField(max_length=100, null=False, default="default")
    amound = models.FloatField(null=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Creation"