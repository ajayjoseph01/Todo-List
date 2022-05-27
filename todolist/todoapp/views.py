from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def signin(request):
    if request.method=="POST":
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            try:
                auth.login(request,user)
                return redirect('/welcome')
                #return HttpResponse('success')
            except:
                pass
        else:
            messages.info(request,'invalid username or password')
            return redirect('/signin')
    return render(request,'signin.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname):
                messages.info(request,'user already exists')
                return redirect('/')     
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                messages.success(request,'user created successfully')
                return redirect('/signin')
        else:
            messages.info(request,'passwords does not match')
            return redirect('/')

    return render(request,'signup.html')

@login_required(login_url='signin')
def welcome(request,id):
    mem=todolists.objects.all().order_by('-id')
    return render(request,'welcome.html',{'mem':mem})

@login_required(login_url='signin')
def profile(request):
    return render(request,'profile.html')

def updateuser(request,id):
    if request.method=="POST":
        users=request.user
        users.username=request.POST['username']
        users.first_name=request.POST['first_name']
        users.last_name=request.POST['last_name']
        users.email=request.POST['email']
        users.save()
        messages.success(request,'profile updated successfully')
        return redirect('/welcome')
    
@login_required(login_url='signin')
def resetpass(request):
    return render(request,'resetpassword.html')

def updatepass(request,id):
    if request.method=="POST":
        users=request.user
        passwd=request.POST['password']
        cpasswd=request.POST['cpassword']
        try:
            if passwd is not None:
                if passwd==cpasswd:
                    users.set_password(passwd)
                    users.save()
                    messages.success(request,'password updated successfully')
                    return redirect('/welcome')
        except:
            pass       
    return redirect('/profile')

def logout(request):
    auth.logout(request)
    messages.success(request,'logout successfully')
    return redirect('/')


def mytodolist(request):
    mem=todolists()
    if request.method=="POST":
        mem.Task=request.POST['task']
        mem.Description=request.POST['description']
        mem.status = 0
        try:
            user= todolists.objects.get(Task=mem.Task)
            context = {'msg': 'Course already exists!!!....  Try to add another course','z':z}
            return render(request,'todolist.html',context)
        except :
            mem.save()
            return redirect('/welcome')
    return render(request,'todolist.html')

def listupdate(request,id):
    if request.method=="POST":
        abc=todolists.objects.get(id=id)
        abc.Description=request.POST['description']
        abc.save()
        return redirect('welcome')
    return render(request,'todolist.html')
   
def listdelete(request,id):
    abc=todolists.objects.get(id=id)
    abc.delete()
    return redirect('welcome')
   

def completestatus(request,id):
    abc=todolists.objects.get(id=id)
    abc.status=1
    abc.save()
    return redirect('welcome')

def search(request):
    given_name=request.POST['search']
    pro=todolists.objects.filter(Task__icontains=given_name)
    #pro=products.objects.filter(description__icontains=given_name)   
    return render(request,'welcome.html',{'pro':pro})
