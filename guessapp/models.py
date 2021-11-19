
from django.db import models



class Roadsign(models.Model):
    sign_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sign_name

