from django.contrib import admin
from .models import User, Supervisor, Agent

# Register your models here.
admin.site.register(User)
admin.site.register(Supervisor)
admin.site.register(Agent)
