from django.shortcuts import render,redirect,reverse
from .models import Job,Category
from django.core.paginator import Paginator
from .form import emp_application,add_New_Job
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import jobFilter
from django.contrib import messages
def jobList(request):
        
        jobs = Job.objects.all()
        
        myfilter = jobFilter(request.GET,queryset=jobs)
        jobs = myfilter.qs
        
        paginator = Paginator(jobs,10)
        
        pNum = request.GET.get("page")
        
        pObjs = paginator.get_page(pNum)
        
        return render(request,'job/allJobs.html', {'jobs':pObjs,'filter':myfilter})
	

def jobDetail(request,slug):
        job = Job.objects.get(slug = slug)
        if request.method == 'POST':
                form = emp_application(request.POST ,request.FILES)
                if form.is_valid():
                        form = form.save(commit=False)
                        form.jobId = job
                        form.employee = request.user
                        form.save()
                        messages.success(request,"Apllied Job Successfully",extra_tags="success")
                        return redirect(reverse("jobs:jobList"))
                
        return render(request, 'job/jobDetail.html', {'job':job})
	
@login_required
def add_job(request):
        add = add_New_Job()
        if request.method == 'POST':
                form = add_New_Job(request.POST,request.FILES)
                print("form valid: ",form.is_valid(), "\n",form.errors)
                if form.is_valid():
                        form = form.save(commit=False)
                        form.employer = request.user
                        form.save()
                        messages.success(request,"Job Added Successfully",extra_tags="success")
                        return redirect(reverse("jobs:jobList"))
        return render(request, 'job/addJob.html', {'addNewJob':add})