from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class SupervisorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is a Supervisor."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_supervisor:
            return redirect("lead-list")
        return super().dispatch(request, *args, **kwargs)
