from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

def index(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = "Freelance Job Alert"
        
        sending = EmailMessage(
        subject = subject,
        body = f"{name}\n{ message,}",
        from_email = email,
        to = [settings.EMAIL_HOST_USER],
        )
        sending.send(fail_silently=False,)
        messages.success(request, "Message sent successfullfuly")     
    return render(request, "index.html")

