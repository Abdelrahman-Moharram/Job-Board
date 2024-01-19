from django import forms
from accounts.models import userTips
from django.contrib.auth.models import User



class updateUser(forms.ModelForm):
    class Meta:
            model = User
            fields = ['first_name','last_name','username','email']

class updateUserTips(forms.ModelForm):
    class Meta:
            model = userTips
            fields = ['userType','userImage','job_title']
            
 
