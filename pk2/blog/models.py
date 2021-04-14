from django.db import models

# Create your models here.
class Block(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField(max_length=50)
  mobile=models.IntegerField()
  city=models.CharField(max_length=50)
 
