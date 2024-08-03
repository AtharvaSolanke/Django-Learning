from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    #return HttpResponse("This is Home page")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("This is About page")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("This is services page")
    return render(request, 'services.html')

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        contact = Contact(name = name, number = number, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    
    return render(request, 'contact.html')