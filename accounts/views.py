from django.shortcuts import redirect, render
from .forms import addUserTips
from .models import userTips
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from random import randint
verficationId = ''


def login_user(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        login(request, user)
                        try:
                                tipsData = userTips.objects.get(user_id=user.id)
                                request.session['image'] = str(tipsData.userImage)
                                request.session['userType'] = tipsData.userType
                                request.session['job_title'] = str(tipsData.job_title)
                                if tipsData.verfication == False:
                                        global verficationId
                                        verficationId = str(user.id) + str(randint(100000,312412412))
                                        send_mail('verfication link is ',"http://127.0.0.1:8000/accounts/{}".format(verficationId),settings.EMAIL_HOST_USER,[user.email],)
                                        messages.warning(request,"Your Email not verfied please check your email",extra_tags="warning")
                        except:
                            pass
                        
                                
                        request.session['id'] = user.id
                        request.session['first_name'] = user.first_name
                        request.session['last_name'] = user.last_name
                        request.session['email'] = user.email
                        request.session['username'] = user.username
                        request.session['is_superuser'] = user.is_superuser
                        request.session['date'] = str(user.date_joined)
                        
                        
                        
                        if user.is_superuser:
                                return redirect("/admin/")
                        else:
                                return redirect("home:index")
                else:
                        messages.warning(request,"Can't Login E-Mail or Password are invalid",extra_tags="warning")

        return render(request,'accounts/login.html', {})

def register(request):
        if request.method == "POST":
                if request.POST['password'] == request.POST['confirm_password']:
                        user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
                        user.first_name = request.POST['first_name']
                        user.last_name = request.POST['last_name']
                        user.save()
                        usertips = addUserTips(request.POST,request.FILES)
                        usertips = usertips.save(commit = False)
                        usertips.user = user
                        usertips.save()
                        username = request.POST['username']
                        password = request.POST['password']
                        user = authenticate(request,username=username,password=password)
                        if user is not None:
                                login(request, user)
                                try:
                                        tipsData = userTips.objects.get(user_id=user.id)
                                        request.session['image'] = str(tipsData.userImage)
                                        request.session['userType'] = tipsData.userType
                                        request.session['job_title'] = str(tipsData.job_title)
                                        if tipsData.verfication == False:
                                                global verficationId
                                                verficationId = str(user.id) + str(randint(100000,312412412))
                                                send_mail('verfication link is ',"http://127.0.0.1:8000/accounts/{}".format(verficationId),settings.EMAIL_HOST_USER,[user.email],)
                                                messages.warning(request,"Your Email not verfied please check your email",extra_tags="warning")
                        
                                except:
                                    pass
                                request.session['id'] = user.id
                                request.session['first_name'] = user.first_name
                                request.session['last_name'] = user.last_name
                                request.session['email'] = user.email
                                request.session['username'] = user.username
                                request.session['is_superuser'] = user.is_superuser
                                messages.success(request,"Your Data has Saved!",extra_tags="success")

                                return redirect("home:index")
                        else:
                                messages.warning(request,"Error while signing you in but your data has Saved!",extra_tags="warning")
                                return redirect("jobs:jobLis")
                else:
                        messages.warning(request,"Password Not The Same",extra_tags="warning")
        return render(request,'accounts/register.html', {'addUserTips':addUserTips()})
@login_required
def logout_user(request):
        logout(request)
        return redirect("home:index")

def verfication(request,verfication):
        print("\n\n\n\n",verfication,"  =  ",verficationId,"\n\n\n\n")
        if verfication == verficationId:
                user = userTips.objects.get(user=request.user)
                user.verfication = True
                user.save()
                messages.success(request,"verfied successfully",extra_tags=verfication)
        else:
                messages.warning(request,"verfied field your link is not valid",extra_tags=verfication)
        return redirect("home:index")
