
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'travel_app/login.html')

def registration(request):
    return render(request, 'travel_app/login-reg.html')

def processreg(request):
    result = User.objects.validate_registration(request.POST)
    if result['status']:    #that means if its true
        request.session['user_id'] = result['user_id']
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error)   
    return redirect('/registration')


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
        "me": User.objects.get(id=request.session['user_id']),
        "users": User.objects.all(),
        "all_trips": Trip.objects.all(),
        # "not_my_trips": Trip.objects.exclude(user_on_trip=request.session['user_id']),
        # "my_trips": Trip.objects.filter(user_on_trip=request.session['user_id']),
        "my_trips": User.objects.get(id=request.session['user_id']).created_trips.all(),
        "joined_trips": User.objects.get(id=request.session['user_id']).trips.all(),
        "others_trip":Trip.objects.exclude(created_by= User.objects.filter(id=request.session['user_id'])).exclude(user_on_trip=User.objects.get(id=request.session['user_id'])) 

    }
    
    return render(request, 'travel_app/success.html', context)

def logout(request):
    request.session.clear() 
    return redirect('/')

def home(request):
    return redirect('/success')
    
def add_travel_plan(request):
    if 'user_id' not in request.session:
        return redirect('/')

    return render(request, 'travel_app/add_trip.html')

def add(request):
    result = Trip.objects.add(request.POST, request.session['user_id'])
    if result['status']:    
        return redirect('/success')
    else:
        for error in result['errors']:
            messages.error(request,error) 
    return redirect('/add_travel_plan') 

def details(request, trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    trip = Trip.objects.get(id=trip_id)
    
    context = {
        "other_users" : User.objects.filter(trips=trip_id).exclude(created_trips=trip_id),
        "current_trip": trip #or without variable "current_trip": Trip.objects.get(id=trip_id)
    }
    print(trip_id)
    return render(request,'travel_app/details.html', context)

def join(request, trip_id):
    Trip.objects.join(trip_id,request.session['user_id'])

    return redirect('/success')

