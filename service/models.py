from django.db import models

# Create your models here.
class Doctor(models.Model):
   
    name = models.CharField( max_length=100)
    img = models.ImageField( upload_to='pics')
    job = models.TextField()
    desc = models.TextField()