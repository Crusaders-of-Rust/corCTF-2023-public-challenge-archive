
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from django_ratelimit.decorators import ratelimit

def login_wrapper(login_func):

    @ratelimit(key='post:username', rate='3/5m')
    def admin_login(request, **kwargs):
        if getattr(request, 'limited', False):  # was_limited
            messages.error(request, 'Too many login attemps, please wait 5 minutes')
            return redirect(reverse("admin:index"))
        else:
            return login_func(request, **kwargs)

    return admin_login