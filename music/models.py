from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class HypoUser(models.Model):
    question = models.CharField(max_length=500)
    mob=models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

