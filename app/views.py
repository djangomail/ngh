from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    nowdate = datetime.now()
    now = nowdate.strftime("%H:%M:%S")
    return render(request, 'app/index.html', {'now':now})