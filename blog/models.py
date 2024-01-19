from django.db import models
from accounts.models import userTips

        
def post_image(instance,filename):
        filename,extention = str(filename).split(".")
        return "media/post/img/{}.{}".format(instance.id,extention)
class Post(models.Model):
	post_image = models.ImageField(upload_to=post_image,blank=True, null=True)
	publisher = models.ForeignKey(userTips, on_delete=models.CASCADE)
	post_title = models.CharField(max_length=150,blank=True, null=True)
	published_at = models.DateTimeField(auto_now=True)
	post_Content = models.TextField(max_length=2000,blank=True, null=True)
	
	def __str__(self):
                return self.post_title+str(self.id)

def comment_image(instance,filename):
        filename,extention = str(filename).split(".")
        return "media/comments/img/{}.{}".format(instance.id,extention)

class comment(models.Model):
        user = models.ForeignKey(userTips,on_delete=models.CASCADE)
        comment = models.CharField(max_length=2000,blank=True, null=True)
        added_at = models.DateTimeField(auto_now=True)
        comment_image = models.ImageField(upload_to=comment_image,blank=True, null=True)
        post = models.ForeignKey(Post, on_delete=models.CASCADE) 
        
        def __str__(self):
                return self.comment+str(self.id)
