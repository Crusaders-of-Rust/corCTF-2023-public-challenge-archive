from django.db import models

class UploadedFile(models.Model):
    file = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.file.path if self.file else "unknown path"
