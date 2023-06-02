from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_supervisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def post_user_creation(sender, instance, created, **kwargs):
    if created:
        Supervisor.objects.create(user=instance)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
