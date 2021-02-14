from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username already taken!'})
            except User.DoesNotExist:
                print('\n\n0000000000\n\n',request.POST['username'],request.POST['confirm_password'])
                user = User.objects.create_user(request.POST['username'],'',request.POST['confirm_password'])
                auth.login(request,user)
                return render(request,'accounts/login.html')
    else:
#        return redirect('home')
        return render(request,'accounts/signup.html')

from django.contrib.auth import authenticate, login as ulogin
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print('\n\n11111111\n\n',user,username,password)
        if user is not None : 
            ulogin(request, user)
#            return HttpResponse(request.user.is_authenticated)
            return render(request,'products/home.html')
        else :
            return(render(request,'accounts/login.html'))

    return(render(request,'accounts/login.html'))

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request,'landing.html')













