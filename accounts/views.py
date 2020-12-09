from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method=='POST':
        print(request.POST['gender'])
        return render(request,'signup.html')

def auth(request): #authentication
    pass

@login_required
def user(request):
    pass
