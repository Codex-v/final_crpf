from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FacedetectUser
from django.conf import settings as s
import os
from django.views.decorators.csrf import csrf_protect



@csrf_protect
def login(request):
    params = {"img": f'{s.BASE_DIR}'}
    if request.method == 'POST':  
        if((FacedetectUser.objects.filter(email=request.POST['email']).exists())):
                user = FacedetectUser.objects.filter(email=request.POST['email'])[0]
                if ((request.POST['password']== user.password)):
                    request.session['id'] = user.id
                    request.session['name'] = user.first_name
                    request.session['surname'] = user.last_name
                    return redirect("/dashboard")
                else:
                    messages.error(request, 'Wrong password.')
                    return render(request, 'login.html',params)
        else:
                messages.error(request, 'Wrong Email')
                return render(request, 'login.html',params)

    else:
        return render(request, 'login.html',params)


