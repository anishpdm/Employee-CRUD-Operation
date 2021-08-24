from django.db import models

# Create your models here.


class Company(models.Model):
    cname = models.CharField(max_length=30, default='')
    caddress= models.CharField(max_length=30,default='')
    cmobile = models.BigIntegerField(default=1)

