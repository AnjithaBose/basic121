from django.db import models

# Create your models here.
class Contact3(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    number=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name

