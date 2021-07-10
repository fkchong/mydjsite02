from django import forms
from .models import book, userprefbook
from django.core.exceptions import ValidationError

class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 10:
            raise ValidationError('Name is too short.')
        return name

class upbform(forms.ModelForm):
    class Meta:
        model = userprefbook
        fields = ('user', 'bookname', 'remark')

    def clean_name(self):
        remark = self.cleaned_data.get('remark')
        if len(remark) < 10:
            raise ValidationError('Remark is too short.')
        return remark

    widgets = {
        'user': forms.Select(attrs={'class': 'form-control'}),
        'bookname': forms.Select(attrs={'class': 'form-control'}),
        'remark': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter remark'})
    }
