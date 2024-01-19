from django.db import models
from django.contrib.auth.models import User
from job.models import Category
from django.db.models.signals import post_save
from django.dispatch import receiver
usersTypes = {
 	('Employer','Employer'),
  	('Employee','Employee'),
}

def image_upload(instance,filename):
        imageFile,extention = filename.split(".")
        return "media/users/%s/%s.%s"%(instance.user,instance.user,extention)

class userTips(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        userType = models.CharField(choices = usersTypes , max_length=20)
        userImage = models.ImageField(default='media/default/job-offer-on-orange-note-260nw-752376046.jpg',upload_to=image_upload)
        verfication = models.BooleanField(default=False)
        job_title = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
        def __str__(self):
            return str(self.user)
        

@receiver(post_save, sender=User)
def create_doctor(sender, instance, **kwargs):
    if kwargs['created']:
        tips = userTips.objects.create(user=instance)
        tips.save()

