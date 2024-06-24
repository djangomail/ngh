from django.shortcuts import render
from datetime import datetime
from .models import Student
# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request, 'app/index.html', {"student":student})
    
def update(request):
    nowdate = datetime.now()
    now = nowdate.strftime("%H:%M:%S")
    return render(request, "partial/time.html", {'now':now})