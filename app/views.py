from django.shortcuts import render
from datetime import datetime
from .models import Student
# Create your views here.
def home(request):
    student = Student.objects.all()
    nowdate = datetime.now()
    now = nowdate.strftime("%H:%M:%S")
    return render(request, 'app/index.html', {'now':now, "student":student})