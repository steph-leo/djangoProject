from django.db import models

# Create your models here.
class Workapp(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    mobilephone = models.IntegerField(null = True)
    startDate = models.DateField(null = True)