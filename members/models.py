from typing import Any
from django.db import models

# Create your models here.

class Accounts(models.Model):

    fname  = models.CharField(max_length=50, null=True)
    lname =  models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.fname

    class Meta :
        verbose_name = "Accounts"
        ordering =["fname"]