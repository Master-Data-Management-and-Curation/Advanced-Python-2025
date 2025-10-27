from django.db import models

# Create your models here.

from django.db import models

class Researcher(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name
