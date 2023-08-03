from django import forms

from .models import UploadedFile
from .services import ImportService

class FileFieldForm(forms.ModelForm):

    uploaded_files = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UploadedFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(),
        }

class UploadedFileAdminForm(forms.ModelForm):
    image_url = forms.CharField(help_text="Enter URL of file to import.")

    class Meta:
        model = UploadedFile
        fields = []

    def clean_image_url(self):
        return ImportService.validate_file_link(self.data['image_url'])
