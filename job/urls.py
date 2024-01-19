
from django.contrib import admin
from django.urls import path , include
from . import views, api

app_name = 'job'
urlpatterns = [
    path('', views.jobList,name="jobList"),
    path('add/', views.add_job,name="addJob"),
    path('<str:slug>', views.jobDetail,name="jobDetail"),
    
    # api
    
    path('browse/',api.job_list_api,name="jobsApi")
]
