from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

# Create your views here.
@csrf_protect
def dashboard(request):        
    return render(request, 'dashboard.html')
