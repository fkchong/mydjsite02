from django import forms
from .models import experience
from django.core.exceptions import ValidationError

class EmpExpModelForm(forms.ModelForm):
    class Meta:
        model = experience
        fields = "__all__"

    def clean_reasonofleaving(self):
        reasonofleaving = self.cleaned_data.get('reasonofleaving')
        if len(reasonofleaving) < 10:
            raise ValidationError('Reason of leaving is too short.')
        return reasonofleaving