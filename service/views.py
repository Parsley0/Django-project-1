from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Doctor
# Create your views here.
def home(request):
    docs= Doctor.objects.all 
    return render(request,'home.html',{'docs':docs})

def contact(request):
    if request.method =="POST": 
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST[' message-subject']
        umessage = request.POST[' umessage']
        
        send_mail(
            message_name,
            message_subject,
            umessage,
            message_email,
            ['nparsley433@gmail.com'],
        )
        
        return render(request,'contact.html',{'message-name':message_name})

    else:
       return render(request,'contact.html',{})
 

