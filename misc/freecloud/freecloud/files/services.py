
import urllib.request
from urllib.parse import urlparse

from django.core.exceptions import ValidationError

class ImportService:
    '''
    Service for handling file imports
    '''
    @staticmethod
    def validate_file_link(file_link):
        scheme_blocklist = ["data", "dict", "file", "ftp", "glob", "gopher"]

        parsed_url = urlparse(file_link)
        
        if parsed_url.hostname == "127.0.0.1":
            raise ValidationError("Invalid hostname")
            

        if parsed_url.scheme in scheme_blocklist:
            raise ValidationError("Invalid scheme")
        
        return file_link

    @staticmethod
    def download_remote_file(validated_link):
        target = urllib.request.urlopen(validated_link)
        return target.read()