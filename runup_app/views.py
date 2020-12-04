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

class GenderChar():
    WOMAN = 'w'
    MAN = 'm'

# Create your views here.

def GetCtg(q_gender):
    #카테고리 메뉴 파트
    q_common = Q(Gender = CtgGenderType.COMMON)
    q_ngen = Q(Gender = CtgGenderType.NONE)

    main_ctgs = MainCategories.objects.filter( q_gender | q_ngen | q_common).order_by('pk')
    sub_ctgs = SubCategories.objects.filter(q_gender | q_common | q_ngen ).order_by('Main')

    return main_ctgs,sub_ctgs

def main(request):
    
    #auth 관련 사항
    #auth 에 따라서 category 펼침 메뉴와 mypage 메뉴가 달라짐

    #로그인 인증
    if request.user.is_authenticated :
        #회원 메뉴 아이템
        
        #회원 성별 획득
        gender = GenderChar.WOMAN if request.user.Gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q( Gender = request.user.Gender )
        
    else :
        #비회원 메뉴 아이템

        #비회원 성별 획득
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN #쿠키 값을 먼저 받는다.
        gender = request.GET.get('gender', gender)
        if (gender == GenderChar.WOMAN or gender == GenderChar.MAN) is not True :
            #잘못된 접근에 대한 정오 w, m이 아닌 경우 w로 정정
            gender = GenderChar.WOMAN    
        q_gender = Q( Gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    
    all_pd = Products.objects.filter(q_gender | Q( Gender=GenderType.COMMON )).order_by('?')
    prod_page = Paginator(all_pd,30) #모든 상품을 30개 보여준다.
    page = prod_page.get_page(1)

    main_ctgs, sub_ctgs = GetCtg(q_gender)

    #메인 포스트 노출 파트

    active_banner_list = Main_banner.objects.filter( Q(Start__gte = timezone.now())| Q(End__lte = timezone.now()) )

    context = {
        'prod_objects' : page, #상품 목록 리스트 Products
        'gender' : gender, #사용자 성별
        'main_post' : active_banner_list, #현재 표시 되는 배너 리스트 쿼리 리스트 Main_banner
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'user_data' : request.user, #유저 메뉴 리스트
    }

    res = render( request, 'main_content.html', context)
    
    #cookie save if user is authenticated
    if request.user.is_authenticated is False : 
        res.set_cookie('gender', gender )

    return res

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