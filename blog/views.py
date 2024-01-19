from django.shortcuts import render
from .models import Post, comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from accounts.models import userTips
def blog(request):
	return render(request, 'blog/blog.html', {'posts':Post.objects.all()})
	

@login_required
def single_blog(request,id):
        post = Post.objects.get(id=id)
        comments = comment.objects.filter(post=post)
        if request.method == "POST":
                add_comment = CommentForm(request.POST,request.FILES)
                if add_comment.is_valid():
	                add_comment = add_comment.save(commit=False)
	                add_comment.user = userTips.objects.get(user=request.user)
	                add_comment.post = post
	                add_comment.save()
        return render(request, 'blog/single_blog.html', {'post':post,'comments':comments})
	