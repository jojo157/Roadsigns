
from django.db import models



class Roadsign(models.Model):
    sign_name = models.CharField(max_length=100)
    photo = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.sign_name

