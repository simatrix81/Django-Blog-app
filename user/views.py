from django.shortcuts import render,redirect,HttpResponsePermanentRedirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
            
            "form" : form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User()
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"başarıyla kaydoldunuz")
        return redirect("index")
    return render(request,"register.html",context)
   
def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
            
            "form" : form
        }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıya Giriş Yaptınız.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
   

def logoutuser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

