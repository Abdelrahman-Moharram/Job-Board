from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
jobType = {
	('Full Time','Full Time'),
	('Part Time','Part Time'),
	('Remotly','Remotly'),
	('Internship','Internship'),
}



class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
	    return self.name




class Job(models.Model):
	
	employer = models.ForeignKey(User,  on_delete=models.CASCADE)
 
	title = models.CharField(max_length=50)
	
	job_type = models.CharField(max_length=50,choices = jobType)

	Description = models.TextField(max_length = 1000)

	publishedAt = models.DateTimeField(auto_now=True)

	Vacancy = models.IntegerField(default=1)

	salary = models.IntegerField(default=0)

	exp = models.IntegerField(default=1)

	cat = models.ForeignKey(Category,verbose_name = "Category Name", on_delete=models.CASCADE)

	image = models.ImageField(upload_to="media/jobs/", default='media/default/job-offer-on-orange-note-260nw-752376046.jpg')
 
 
	slug = models.SlugField(blank=True,null=True)
 
	def save(self, *args, **kwargs):
            self.slug = slugify(self.title+str(self.id))
            super(Job,self).save(*args,**kwargs)

	def __str__(self):
	    return self.title


def cv_upload(instance,filename):
        cvFile,extention = filename.split(".")
        return "media/job_applications/%s/%s.%s"%(instance.employee,instance.employee,extention)

class job_application(models.Model):
        employee = models.ForeignKey(User,  on_delete=models.CASCADE)
        jobId = models.ForeignKey(Job, verbose_name=("Job"), on_delete=models.CASCADE)
        protifolio = models.URLField(max_length=200)
        cv = models.FileField(upload_to=cv_upload)
        coverLetter = models.TextField(max_length=500)
        applyAt = models.DateTimeField(auto_now=True)

        def __str__(self):
        	return str(self.employee)
	