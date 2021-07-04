from django.db import models
from django import  forms
from .models import Groups,Student

class CreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'