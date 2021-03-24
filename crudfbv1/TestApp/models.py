from django.db import models

# Create your models here.
class Parcel(models.Model):
    billno = models.IntegerField()
    shippername = models.CharField(max_length = 20)
    rate = models.FloatField()
    
