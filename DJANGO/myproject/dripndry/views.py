from django.shortcuts import render, redirect
from dripndry.forms import UserForm
from dripndry.forms import orderform
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from dripndry.models import dripndry
from dripndry.models import order

def index(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request, 'gallery.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def welcome(request):
    return render(request,'welcome.html')
def success(request):
    return render(request,'success.html')

def ordering(request):
    ordered = False
    if request.method == 'POST':
        order_form = orderform(data = request.POST)

        if order_form.is_valid():
	    #user.password = make_password(user.cleaned_data['password'])
            user = order_form.save()
            user.save()
            ordered = True
            return render(request,'success.html')#, {'order_form' : order_form, 'ordered' : ordered})
        else:
            print(order_form.errors)

    else:
        order_form = orderform()

    return render(request,'ordering.html', {'order_form' : order_form, 'ordered' : ordered})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)

        if user_form.is_valid():
	    #user.password = make_password(user.cleaned_data['password'])
            user = user_form.save()
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'register.html', {'user_form' : user_form, 'registered' : registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')
        a = dripndry.objects.filter(username=username).exists()
        b = dripndry.objects.filter(password=password).exists()
        
        if a and b:
            return HttpResponseRedirect('ordering')

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'user_login.html')
def admin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')
        a = dripndry.objects.filter(username=username).exists()
        b = dripndry.objects.filter(password=password).exists()
        
        if a and b:
            return HttpResponseRedirect('post1')

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'admin_login.html')

def post(request):
	allorderings= order.objects.all()
	context= {'allorderings': allorderings}
	return render(request, 'post.html', context)
def post1(request):
	allorderings= order.objects.all()
	context= {'allorderings': allorderings}
	return render(request, 'post1.html', context)









