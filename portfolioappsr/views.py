from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please Login to Contact us")
        return render(request,"login.html")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['num']
        desc=request.POST['desc']
        if len(phone)>12 or len(phone)<10:
            messages.warning(request,"Please enter 10 digit phone number")
            return redirect('/contact')
        query=Contact(name=name,email=email,phone=phone,description=desc)
        query.save()
        messages.success(request,"Thanks for contacting us! We will get back to you soon!")
        return redirect('/contact')
    return render(request,"contact.html")

def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        #validate password & confirm password
        if pass2 != pass1:
            messages.error(request,"Password not matching")
            return redirect('/signup')

        #print(fname,lname,email,pass1,pass2)
        #messages.info(request,f'{fname},{lname},{email},{pass1},{pass2}')
        
        #i am validating user exist or not with the same email & username
        try:
            if User.objects.get(username=email):
                messages.warning(request,"User Already Exist")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email Already Exist")
                return redirect('/signup')
        except:
            pass

        user=User.objects.create_user(email,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,"Signup Success")
        return redirect('/login')
        # messages.success(request,"Enter your details")
        # messages.error(request,"Re-Enter your details")
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        user=authenticate(username=email,password=pass1)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials, Try again!")
            return redirect('/login')
        
    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')


def exploremore(request):
    return render(request,"index.html")

def projects(request):
    return render(request,"projects.html")

def certificates(request):
    return render(request,"certificates.html")

def blogs(request):
    return render(request,"blogs.html")
