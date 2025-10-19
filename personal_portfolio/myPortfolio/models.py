from django.db import models

# Create your models here.
class Guest(models.Model):
    f_name = models.CharField(max_length=15,blank=False)
    l_name = models.CharField(max_length=15,blank=False)
    email = models.EmailField(max_length=256,blank=False)