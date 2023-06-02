from django.db import models
from leads.models import Agent
from leads.models import Lead
from products.models import Product


class Order(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    details = models.TextField(max_length=400)
    agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} - {self.agent}"
