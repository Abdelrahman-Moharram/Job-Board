from django import forms
from .models import employee



class emp_application (forms.ModelForm):
        class Meta:
                model = employee
                fields = ['name', 'email', 'protifolio', 'cv', 'coverLetter']


	