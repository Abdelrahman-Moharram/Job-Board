from django import forms
from .models import userTips
from django.contrib.auth.models import User


class addUserTips(forms.ModelForm):
    class Meta:
            model = userTips
            fields = ['userType','userImage','job_title']
            
 
