from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import AccountForm

# Create your views here.

def log_in(request):
    """
    log_in view
    """
    redir_url = request.GET.get('next','index')
    if request.user.is_authenticated:
        return redirect(redir_url)
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method =='POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            redir_url= request.POST['next'] if request.POST['next'] != '' else 'index'
            return redirect(redir_url)
        else :
            if redir_url != 'index':
                return render(request,'login.html',{'error':'login failed','next':request})
            else :
                return render(request,'login.html',{'error':'login failed'})
    return redirect('index')

def signup(request):
    if request.user.is_authenticated :
        return redirect('index')
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method=='POST':
        #print(request.POST)
        form = AccountForm(request.POST)
        if form.is_valid() :
            new_user = form.save()
            new_user.save()
            login(request,new_user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else :
            return render(request,'signup.html',{'errors':form.errors})
        return render(request,'signup.html')

@login_required
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

@login_required
def userinfo(request):
    if request.user.is_authenticated:
        context = {
            'User' : request.user
        }
        return render(request,'userinfo.html',context)
    else :
        return redirect('index')
