from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50,default='No NAME',blank=True)
    empcode = models.CharField(max_length=50,default='No NAME',blank=True)
    empdesig = models.CharField(max_length=50)
    empsalary = models.CharField(max_length=50, default='No NAME', blank=True)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   
