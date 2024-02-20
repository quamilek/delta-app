from django import forms
from projects.models import Project 

class ImportProjectForm(forms.ModelForm):
    
    projectFile = forms.FileField()

    class Meta:
        model = Project
        fields = ['client',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-select the first client by default
        self.fields['client'].initial = self.fields['client'].queryset.first()