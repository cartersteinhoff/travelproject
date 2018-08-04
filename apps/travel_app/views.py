
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'travel_app/login-reg.html')

def processreg(request):
    result = User.objects.validate_registration(request.POST)
    if result['status']:    #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)   
    return redirect('/')


def processlog(request):
    result = User.objects.validate_login(request.POST)
    if result['status']: #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)    
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
            "me": User.objects.get(id=request.session['user_id'])
    }
    
    return render(request, 'travel_app/success.html', context)

def logout(request):
    request.session.clear() 
    return redirect('/')
