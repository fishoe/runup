from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout
from .forms import AccountForm
from .models import Users
from django.conf import settings

# Create your views here.

def log_in(request):
    redir_url = request.GET.get('next','index')
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method =='POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect(redir_url)
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
        if(form.is_valid()):
            a = form.save()
            # res = "id : " + a.username + "<br/>\n"
            # res += "name : " + a.Name + "<br/>\n"
            # res += "P.N : " + a.Contact + "<br/>\n"
            # res += "Email : " + a.Email + "<br/>\n"
            # res += f"Birth : {a.Birth} <br/>\n"
            # res += f"Gender : {a.Gender} <br/>"
            a.save()
            login(request,a)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else :
            return render(request,'signup.html',{'errors':form.errors})
        return render(request,'signup.html')

@login_required
def user(request):
    if request.user.is_authenticated:
        context = {
            'User' : request.user
        }
        return render(request,'userinfo.html',context)
    else :
        return redirect('index')