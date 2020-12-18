from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name = 'main'), #메인 페이지
    path('index', views.main, name = 'index'), #메인 페이지
    path('<int:product_id>', views.product_pg, name = 'product'), #제품 페이지
    path('likes', views.likes, name = 'likes'), #좋아요 리스트
    path('<int:product_id>/like',views.like, name = 'like'), #좋아요 action 대응 ajax url
    path('best', views.best, name = 'best_page'), #베스트 리스트 페이지
    path('sale', views.sale, name = 'sale_page'), #세일즈 리스트 페이지
    path('brandrank', views.brandrank, name = 'brand_page'), #브랜드 리스트 페이지
    path('category', views.category_pg, name = 'category'), #카테고리 페이지
    path('scatch',views.styleCatch, name = 'styleCatch'), #스타일캐치 페이지
    path('search', views.searchPage, name='searchPage'), #검색 페이지
    path('scatch_res', views.analyzing, name='analyze'), #스타일캐치 분석 페이지

    # #이하 테스트용 url
    # path('test', views.test, name = 'test'),
    # path('upload', views.uploadimg, name = 'up'),
]