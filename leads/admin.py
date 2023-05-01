from django.contrib import admin

from .models import User, Supervisor, Agent, Lead


admin.site.register(User)
admin.site.register(Supervisor)
admin.site.register(Agent)
admin.site.register(Lead)
