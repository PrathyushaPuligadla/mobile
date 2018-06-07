from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default='')
    phone = models.IntegerField(default='')
    emailid = models.CharField(max_length=100, default='')

def __str__(self):
    return self.name