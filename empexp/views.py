from django.shortcuts import render
from django.views.generic import FormView
from .forms import EmpExpModelForm
from django.contrib import messages

# Create your views here.
class MyEmpExpFormView(FormView):
    form_class = EmpExpModelForm
    template_name = "empexp/index.html"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Save successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Error in form...')
        return super().form_invalid(form)