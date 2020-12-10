from django.urls import path
from . import views

urlpatterns=[
    path('userinfo', views.user, name = 'userinfo'), #유저 정보 페이지
    path('login', views.log_in, name = 'login'), #로그인 페이지
    path('signup', views.signup, name = 'signup'), #가입 페이지
]