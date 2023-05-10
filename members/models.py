from django.db import models

# Create your models here.

class Accounts(models.Model):

    fname  = models.CharField(max_length=50)
    lname =  models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.fname

    class Meta :
        verbose_name = "Accounts"
        ordering =["fname"]