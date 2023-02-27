from django import forms
from .models import FileUp
from django.contrib.auth.models import User

class FileForm(forms.ModelForm):

    class Meta:
        model = FileUp
        fields = ['file_name', 'file_upper']
