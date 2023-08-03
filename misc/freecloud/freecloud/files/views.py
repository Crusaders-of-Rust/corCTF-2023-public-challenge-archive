from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import FileFieldForm
from .models import UploadedFile


@method_decorator(csrf_exempt, name='dispatch')
class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'templates/base.html'
    # TODO: find a way to serve this page directly
    success_url = '/?page=templates/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state = self.request.GET.get('page', 'templates/upload.html')
        context['page'] = state
        return context
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')

        if form.is_valid():
            # Should in theory make it possible to upload multiple files at once
            for file in files:
                UploadedFile(file=file).save()
            return self.form_valid(form)
        return self.form_invalid(form)