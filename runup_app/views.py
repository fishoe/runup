from django.shortcuts import render
from .models import SubCategories, MainCategories, Brands, Products, Users, Similarities
from .models import Review_rates, Reviews, Product_Likes, Recommend_result
from .models import Main_banner
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

#constants
class GenderType():
    COMMON = 0
    WOMAN = 1
    MAN = 2

class CtgGenderType():
    WOMAN = 1
    MAN = 2
    COMMON = 3
    NONE = 4

# Create your views here.

def main(request):
    
    #auth 관련 사항
    #auth 에 따라서 category 펼침 메뉴와 mypage 메뉴가 달라짐
    q_gender = None

    #로그인 인증
    if request.user.is_authenticated :
        #로그인시
        gender = 'w' if request.user.Gender == GenderType.WOMAN else 'm'
    else :
        #페이지 아이템 출력 
        #비회원 기준으로 설정
        gender = request.GET.get('gender','w')
    
    if (gender is 'w' or gender is 'm') is not True :
        #잘못된 접근 출력?
        gender = 'w' 
    q_gender = Q( Gender = GenderType.WOMAN if gender == 'w' else GenderType.MAN )
    
    all_pd = Products.objects.filter(q_gender|Q( Gender=GenderType.COMMON )).order_by('?')
    prod_page = Paginator(all_pd,30) #모든 상품을 30개 보여준다.
    page = prod_page.get_page(1)

    #카테고리 메뉴 파트
    q_common =  Q(Gender = CtgGenderType.COMMON)
    q_ngen = Q(Gender = CtgGenderType.NONE)

    main_ctgs = MainCategories.objects.filter( q_gender | q_ngen | q_common).order_by('pk')
    sub_ctgs = SubCategories.objects.filter(q_gender | q_common | q_ngen ).order_by('Main')

    #메인 포스트 노출 파트

    active_banner_list = Main_banner.objects.filter( Q(Start__gte = timezone.now())| Q(End__lte = timezone.now()) )

    #로그인 펼침 메뉴 부분

    #Auth 구현 전까지 미구현
    user_menu_list = None

    context = {
        'prod_objects' : page, #상품 목록 리스트 Products
        'gender' : gender, #사용자 성별
        'main_post' : active_banner_list, #현재 표시 되는 배너 리스트 쿼리 리스트 Main_banner
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'user_menu' : user_menu_list, #유저 메뉴 리스트
    }

    return render( request, 'main_content.html', context)

def recommend(request):
    #auth 확인 후 로그인 페이지 리다이렉트
    #파일 읽기 후 페이지에서 리사이징 js 이용
    #파일 업로드 후 추천 시스템 모듈 이용
    #결과 값을 통한 제품 추천 페이지 이동
    return None

def product_pg(request):
    #제품 디테일 페이지 관련
    return None

def nonepg(request):
    return None

def test(request):
    return render(request,"test.html",{'var':'chooohada _ teacher'})