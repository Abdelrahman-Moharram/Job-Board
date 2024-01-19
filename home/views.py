from django.shortcuts import redirect, render
from job.models import Job,job_application
from accounts.models import userTips
from django.contrib.auth.models import User
from .forms import updateUser, updateUserTips
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
        jobs = Job.objects.all()
        jobs = jobs[:10]
        return render(request,'home/index.html', {'jobs':jobs})




def user_profile(request,username):
        user = User.objects.get(username=username)
        usertipsData = userTips.objects.get(user=user)
        jobs = Job.objects.filter(employer=user)
        apps = job_application.objects.filter(employee=user)

        return render(request,"home/profile.html",{'user':user,'userTips':usertipsData,'jobs':jobs,'apps':apps})
@login_required
def edit_user(request,username):
        usertipsData = userTips.objects.get(user=request.user)
        
        userform = updateUser(instance=request.user)
        usertips = updateUserTips(instance=usertipsData)
        if username != request.user.username:
                return redirect("home:edit_user",username=request.user.username)
        else:
                if request.method == 'POST':
                        userform = updateUser(request.POST,instance=request.user)
                        usertips = updateUserTips(request.POST,request.FILES,instance=usertipsData)
                        
                        if userform.is_valid() and usertips.is_valid():
                                userform.save()
                                usertips = usertips.save(commit=False)
                                usertips.user = request.user
                                usertips.save()
                                
                                tipsData = userTips.objects.get(user = request.user)
                                request.session['image'] = str(tipsData.userImage)
                                request.session['userType'] = tipsData.userType
                                request.session['job_title'] = str(tipsData.job_title)
                                request.session['id'] = request.user.id
                                request.session['first_name'] = request.user.first_name
                                request.session['last_name'] = request.user.last_name
                                request.session['email'] = request.user.email
                                request.session['username'] = request.user.username
                                request.session['is_superuser'] = request.user.is_superuser
                                messages.success(request,"Data UPDATED Successfully",extra_tags="success")
                                return redirect("/"+request.user.username)
                        
                        
        return render(request, "home/edit_profile.html",{'user':userform,'userTips':usertips,})