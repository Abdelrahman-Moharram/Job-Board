from django import forms
from .models import job_application,Job



class emp_application (forms.ModelForm):
        class Meta:
                model = job_application
                fields = ( 'protifolio', 'cv', 'coverLetter')


class add_New_Job(forms.ModelForm):
        class Meta:
                model = Job
                fields = ('title','job_type','Description','Vacancy','salary','exp','image','cat')
