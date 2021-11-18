from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media')

class Roadsign(models.Model):
    sign_name = models.CharField(max_length=100)
    photo = models.ImageField(storage=fs, blank=True)

    def __str__(self):
        return self.sign_name

