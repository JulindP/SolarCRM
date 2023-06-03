from django.db import models

from agents.models import Supervisor


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
