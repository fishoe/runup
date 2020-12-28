from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.db.models import Q

from runup_app.views import GenderType, GenderChar, GetCtg
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
        gender = request.COOKIES.get('gender', 'w')
        q_gender = Q(gender=GenderType.WOMAN if gender ==GenderChar.WOMAN else GenderType.MAN)

        main_ctgs, sub_ctgs = GetCtg(q_gender)
        context = {
            'gender': gender,  # 사용자 성별
            'main_ctgs': main_ctgs,  # 메인 카테고리 리스트
            'sub_ctgs': sub_ctgs,  # 서브 카테고리 리스트
            'user': request.user,  # 유저 메뉴 리스트
        }
        return render(request,'login.html',context=context)
    elif request.method =='POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            redir_url= request.POST['next'] if request.POST['next'] != '' else 'index'
            response = redirect(redir_url)
            u_gender = GenderChar.WOMAN if user.gender == GenderType.WOMAN else GenderChar.MAN
            response.set_cookie('gender', u_gender)
            return response
        else :
            if redir_url != 'index':
                return render(request,'login.html',{'error':'login failed','next':request})
            else :
                return render(request,'login.html',{'error':'login failed'})
    return redirect('index')

def signup(request):
    if request.user.is_authenticated :
        return redirect('index')
    if request.method == 'GET':
        gender = request.COOKIES.get('gender', 'w')
        q_gender = Q(gender=GenderType.WOMAN if gender ==GenderChar.WOMAN else GenderType.MAN)

        main_ctgs, sub_ctgs = GetCtg(q_gender)
        context = {
            'gender': gender,  # 사용자 성별
            'main_ctgs': main_ctgs,  # 메인 카테고리 리스트
            'sub_ctgs': sub_ctgs,  # 서브 카테고리 리스트
            'user': request.user,  # 유저 메뉴 리스트
        }
        return render(request, 'signup.html',context=context)
    elif request.method == 'POST':
        #print(request.POST)
        form = AccountForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            login(request,new_user)
            u_gender = GenderChar.WOMAN if new_user.gender == GenderType.WOMAN else GenderChar.MAN
            response = redirect(settings.LOGIN_REDIRECT_URL)
            response.set_cookie('gender',u_gender)
            return response
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
        gender = request.COOKIES.get('gender', 'w')
        q_gender = Q(gender=GenderType.WOMAN if gender ==GenderChar.WOMAN else GenderType.MAN)

        main_ctgs, sub_ctgs = GetCtg(q_gender)
        context = {
            'gender': gender,  # 사용자 성별
            'main_ctgs': main_ctgs,  # 메인 카테고리 리스트
            'sub_ctgs': sub_ctgs,  # 서브 카테고리 리스트
            'user': request.user,  # 유저 메뉴 리스트
        }
        return render(request,'userinfo.html',context)
    else :
        return redirect('index')
