from django.contrib import admin
from django.core.files.base import ContentFile

from .forms import UploadedFileAdminForm
from .models import UploadedFile
from .services import ImportService

class UploadedFileAdmin(admin.ModelAdmin):
    form = UploadedFileAdminForm

    def save_model(self, request, obj, form, change):
        if obj.pk:
            obj.save()
            return

        url = form.cleaned_data.get('image_url')

        file_content = ImportService.download_remote_file(url)
        
        if file_content:
            file_name = url.split("/")[-1]
            uploaded_file = UploadedFile()
            uploaded_file.file.save(file_name, ContentFile(file_content))
            uploaded_file.save()

admin.site.register(UploadedFile, UploadedFileAdmin)
