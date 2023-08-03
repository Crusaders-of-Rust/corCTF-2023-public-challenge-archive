from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .decorators import login_wrapper

admin.autodiscover()
admin.site.login = login_wrapper(admin.site.login)

# Random admin url for security reasons
admin_url = settings.ADMIN_URL + "/"
print(f"Admin URL: {admin_url}")

urlpatterns = [
    path('', include('files.urls')),
    path(admin_url, admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)