from __future__ import unicode_literals
from django.db import models

class hyUser(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    password = models.CharField(max_length=100)
    company=models.CharField(max_length=500)
    officeEmail=models.CharField(max_length=100)
    mob=models.IntegerField()
    where= models.CharField(max_length=500)

    def __str__(self):
        return self.fname


