from django.db import models

# Create your models here.
class ImageMetadata(models.Model):
    path = models.CharField(max_length=256)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return self.path

class InstrumentMetadata(models.Model):
    device_id = models.CharField(primary_key=True)
    device_name = models.CharField(max_length=42)

    def __str__(self):
        return self.device_name