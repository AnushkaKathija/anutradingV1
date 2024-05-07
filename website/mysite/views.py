from django.shortcuts import render, HttpResponse
from datetime import datetime
from mysite.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        companyName = request.POST.get('companyName')
        personName = request.POST.get('personName')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        message = request.POST.get('message')
        contact = Contact(companyName = companyName, personName = personName, email = email, phoneNumber = phoneNumber, message = message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    return render(request, 'products.html')

def mechanical(request):
    return render(request, 'mechanical.html')

def fibreoptics(request):
    return render(request, 'fibreoptics.html')

def abrasivematerials(request):
    return render(request, 'abrasivematerials.html')

def electricals(request):
    return render(request, 'electricals.html')

def instrumentation(request):
    return render(request, 'instrumentation.html')

def telecommunication(request):
    return render(request, 'telecommunication.html')

def brands(request):
    return render(request, 'brands.html')
