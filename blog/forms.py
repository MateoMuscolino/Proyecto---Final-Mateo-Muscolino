from django import forms
from .models import Opinion

class EditarOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['libro', 'opinion']