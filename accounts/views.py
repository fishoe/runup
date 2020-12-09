from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountForm
from .models import Users

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=='GET':
        s = request.path
        return render(request,'signup.html')
    elif request.method=='POST':
        print(request.POST)
        form = AccountForm(request.POST)
        if(form.is_valid()):
            user_new = UserCreationForm(req)
        else :
            return request(request,'signup.html')
        return render(request,'signup.html')

def auth(request): #authentication
    pass

@login_required
def user(request):
    pass
