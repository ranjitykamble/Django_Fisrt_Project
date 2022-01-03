from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.

def index(request):
    context = {
        "variable1": "This is sent",
        "variable2": "This is Ranjit"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page");


def practice(request):
    context = {
        "variable": "This is Created Variable"
    }
    return render(request, "practice.html", context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()


    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')
