from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name = 'main'), #메인 페이지
    path('index', views.main, name = 'index'), #메인 페이지
    path('<int:product_id>', views.nonepg, name = 'product'), #제품 페이지
    path('likes', views.nonepg, name = 'likes'), #좋아요 리스트
    path('<int:product_id>/like',views.nonepg, name = 'like'), #좋아요 action 대응 ajax url
    path('best', views.nonepg, name = 'best_page'), #베스트 리스트 페이지
    path('sale', views.nonepg, name = 'sale_page'), #세일즈 리스트 페이지
    path('brandrank', views.nonepg, name = 'brand_page'), #브랜드 리스트 페이지
    path('recommend', views.nonepg, name = 'recommend'), #추천 시스템 페이지
    path('searchresult', views.nonepg, name = 'result'), #검색 결과 페이지
    path('category', views.nonepg, name = 'category'), #카테고리 페이지
    path('login', views.nonepg, name = 'login'), #로그인 페이지
    path('signup', views.nonepg, name = 'signup'), #가입 페이지
    path('userinfo', views.nonepg, name = 'userinfo'), #유저 정보 페이지

    path('test', views.test, name = 'test')
]