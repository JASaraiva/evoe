from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    item            = models.CharField(max_length=200)
    user            = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    checked         = models.BooleanField(default=False)

    def __str__(self):
        return item