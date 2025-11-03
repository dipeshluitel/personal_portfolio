from django.db import models

# Create your models here.
class Guest(models.Model):
    firstname = models.CharField(max_length=15,blank=False, verbose_name='enter your name')
    lastname = models.CharField(max_length=15,blank=False)
    email = models.EmailField(max_length=256,blank=False)
    content = models.TextField(verbose_name='Additional Message')
    # dropdown = models.drop