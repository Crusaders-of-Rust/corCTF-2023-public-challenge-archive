from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileFieldFormView.as_view(), name='upload_file'),
]
