from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from app.models import landModel, Contact
from datetime import datetime, date
from django.http import FileResponse
from django.contrib import messages
import os

# Create your views here.
def index(request):
    objects = landModel.objects.all()
    NumberOfEntry = len(objects)
    return render(request, 'landpost/index.html', {'posts' : objects, 'entries' : NumberOfEntry})

def add_post(request):
    if request.method == "POST":
        details = landModel()
        details.ownerName = request.POST.get('inputFirstName') + request.POST.get('inputLastName')
        details.irrigationSource = request.POST.get('inputirrigationSource')
        details.climateCond = request.POST.get('inputclimateCond')
        details.cropHistory = request.POST.get('inputcropHistory')
        details.address = request.POST.get('inputAddress') + " " + request.POST.get('inputAddress2') + " " + request.POST.get('inputCity') + " " + request.POST.get('inputState') + " " + request.POST.get('inputZip')
        details.landSize = request.POST.get('inputlandSize')
        details.soilType = request.POST.get('inputsoilType')
        details.pub_date = datetime.now()
        # if len(request.FILES) != 0:
        details.thumbnail = request.POST.get('img')
        # details = landModel(ownerName=ownername, irrigationSource=irrigationSource, climateCond=climateCond,
                            # cropHistory=cropHistory, address=address, landSize=landSize, soilType=soilType, pub_date=pub_date, thumbnail=thumbnail)
        details.save()
        return redirect('/')
        # messages.success(request, 'Post saved successfully')
    return render(request, 'landpost/add_post.html')

def landDetails(request):
    return render(request, 'landpost/details.html')

def about(request):
    filepath = os.path.join('static', 'Pratham Khandelwal.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')