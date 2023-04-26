from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def post_save_agent_creation(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(instance=User)


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    agent = models.ForeignKey(Agent, models.CASCADE)
