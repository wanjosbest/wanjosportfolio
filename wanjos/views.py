from django.shortcuts import render,HttpResponse
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        service = request.POST.get("service")
        subject = "Freelance Job Alert"

        if subject and name and email and message and service:
            try:
                send_mail(subject, message,name,service, settings.EMAIL_HOST_USER, [email])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "index.html", context)
"""
def index(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        service = request.POST.get("service")
        savetodatabase = Contact.objects.create(name =name, email = email, message=message,service_id = service)
        savetodatabase.save()
        return HttpResponse("Message sent succesfully!, I will respond to you Through Email")
        

    return render (request, "index.html")
"""
