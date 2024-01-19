from django.shortcuts import render
from django.core.mail import send_mail
from  django.conf import settings
from django.contrib import messages
def Contact(request):
        if request.method == 'POST':
                send_mail(
			request.POST['subject'],
   			request.POST['message'],
			settings.EMAIL_HOST_USER,
			[request.POST['email']],
		)
                messages.success(request,"Email Successfully Sent to '{}' check your inbox please!".format(request.POST['email']),extra_tags="success")
        return render(request, 'contact/contact.html', {})
	