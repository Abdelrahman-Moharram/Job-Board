from django.contrib import admin


from .models import Job,Category, job_application

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(job_application)