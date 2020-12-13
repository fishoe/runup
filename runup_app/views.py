from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.utils import timezone
from django.http import Http404, HttpResponseNotFound, JsonResponse
from django.db.models import Sum,Count    # DB aggregation 사용

from config.settings import DEBUG

from .models import subcategories, maincategories, brands, products, similarities
from .models import review_rates, reviews, product_likes, scatch_result
from .models import main_banner 
from .forms import UploadImgForm
#constants
class const():
    ITEMS_PER_PAGE=30

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
    #카테고리 메뉴
    q_common = Q(gender = CtgGenderType.COMMON)
    q_ngen = Q(gender = CtgGenderType.NONE)

    main_ctgs = maincategories.objects.filter( q_gender | q_ngen | q_common).order_by('pk')
    sub_ctgs = subcategories.objects.filter(q_gender | q_common | q_ngen ).order_by('main')

    return main_ctgs,sub_ctgs

def main(request):

    #로그인 인증
    if request.user.is_authenticated :
        #회원 메뉴 아이템
        #회원 성별 획득
        gender = request.user.gender
        q_gender = Q( gender = request.user.gender )
    else :
        #비회원 메뉴 아이템
        #비회원 성별 획득
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN #쿠키 값을 먼저 받는다.
        gender = request.GET.get('gender', gender)
        if (gender == GenderChar.WOMAN or gender == GenderChar.MAN) is not True :
            #잘못된 접근에 대한 정오 w, m이 아닌 경우 w로 정정
            gender = GenderChar.WOMAN
        q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    
    flt_opt = request.GET.get('flt','?')
    all_pd = products.objects.filter(q_gender | Q( gender=GenderType.COMMON )).order_by(flt_opt)#정렬 옵션에 대한 것
    prod_page = Paginator(all_pd, const.ITEMS_PER_PAGE ) #모든 상품을 30개 보여준다.
    page = prod_page.get_page(1)

    main_ctgs, sub_ctgs = GetCtg(q_gender)

    #메인 포스트 노출 파트

    active_banner_list = main_banner.objects.filter( Q(start__gte = timezone.now())| Q(end__lte = timezone.now()) )

    context = {
        'contents' : page, #상품 목록 리스트 Products
        'gender' : gender, #사용자 성별
        'main_post' : active_banner_list, #현재 표시 되는 배너 리스트 쿼리 리스트 Main_banner
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'user' : request.user, #유저 메뉴 리스트
    }

    res = render( request, 'main_content.html', context)
    
    #cookie save if user is authenticated
    if request.user.is_authenticated is False : 
        res.set_cookie('gender', gender )
    return res

def category_pg(request):
    #auth
    if request.user.is_authenticated :
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
        q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    try :
        sub_ctg_id = int(request.GET.get('s_ctg',-1))
        flt = request.GET.get('flt','?')
        if sub_ctg_id == -1 :
            main_ctg_id = int(request.GET.get('m_ctg',-1))
            main_ctg = maincategories.objects.get(id = main_ctg_id)
            sub_ctg = None
            ctg_pd_list = products.objects.filter( Q(category__main=main_ctg_id) & (q_gender | Q(gender=GenderType.COMMON) ) )#.order_by(flt) 
        else :
            sub_ctg = subcategories.objects.get( id = sub_ctg_id )
            if sub_ctg.gender != CtgGenderType.COMMON and sub_ctg.gender != CtgGenderType.NONE:
                gender = GenderChar.WOMAN if sub_ctg.gender == CtgGenderType.WOMAN else GenderChar.MAN
            main_ctg = sub_ctg.main
            ctg_pd_list = products.objects.filter( Q(category=sub_ctg) & (q_gender | Q(gender=GenderType.COMMON) ))#.order_by(flt) #todo
        paginator = Paginator(ctg_pd_list, const.ITEMS_PER_PAGE )
        page = paginator.get_page(1)
    except ValueError as e:
        raise Http404('invalid value')
    except maincategories.DoesNotExist as e :
        raise Http404('not m_ctg')
    except subcategories.DoesNotExist as e :
        raise Http404('not s_ctg')

    main_ctgs, sub_ctgs = GetCtg(q_gender)

    #print(request.user)

    context = {
        'user' : request.user , # 유저정보
        'contents' : page , #상품 목록 리스트 Products
        'm_ctg': main_ctg ,
        's_ctg' : sub_ctg ,
        's_ctg_friends' : main_ctg.sub_ctgs.all(), #현 카테고리 메인의 친구들
        'gender' : gender, #사용자 성별
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'user' : request.user, #유저 메뉴 리스트
    }
    if request.is_ajax():
        ctg_page = int(request.GET.get('page',-1))
        context['contents']=paginator.page(ctg_page)
        return render(request,'ctg_content.html',context=context)
    else :
        return render(request,'ctg_content.html', context=context )

def product_pg(request, product_id):
    try :
        pd = products.objects.get( id=product_id )
    except products.DoesNotExist as e:
        raise Http404(e)
    contents = similarities.objects.filter(target_prod=pd).order_by('-sim_val') 

    #리프레시 검사(리프레시를 이용한 뷰카운트 조작 방지 구현)
    pd.view_count += 1

    #제품 디테일 페이지 관련
    if request.user.is_authenticated :
        #회원
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
        if pd.gender != GenderType.COMMON :
            gender = GenderChar.WOMAN if pd.gender == GenderType.WOMAN else GenderChar.MAN
    
    q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)

    context = {
        'user' : request.user , # 유저정보
        'main' : pd,
        'contents' : contents,
        'gender' : gender,
        'main_ctgs' : main_ctgs,
        'sub_ctgs' : sub_ctgs,
    }

    res = render(request,'sub_content.html',context=context)
    if request.user.is_authenticated is False : 
        res.set_cookie('gender', gender )
    return res

from django.contrib.auth.decorators import login_required
@login_required
def styleCatch(request):
    if request.user.is_authenticated :
        return render(request, 'styleCatch.html')

# from django.views.decorators.csrf import csrf_exempt, csrf_protect
@login_required
def analyzing(request):
    if request.user.is_authenticated and request.method == 'POST': 
        
        #성별을 가져옵니다.
        gender = request.user.gender
        q_gender = Q( gender = gender )

        #request의 포스트 데이터의 validate 체크
        form = UploadImgForm(request.POST, request.FILES)
        if form.is_valid() :
            img = request.FILES['photo'] if 'photo' in request.FILES else request.FILES['album']

            #암튼 함수를 돌렸음 암튼 그럼

            s_result = scatch_result(user=request.user, img= img, result='Nothing')
            s_result.save()
        else :
            return HttpResponseNotFound("Not valid Image")
        #대충 알고리즘을 돌렸습니다
        class ACLS():
            pass
        main = ACLS()
        main.img_url = s_result.img.url 

        main_ctgs, sub_ctgs = GetCtg(q_gender)
        smpl_pd = products.objects.all().order_by('?')[0]
        contents = smpl_pd.target_prod.all().order_by('-sim_val')

        context = {
            'user' : request.user , # 유저정보
            'main' : main ,
            'contents' : contents ,
            'gender' : gender ,
            'main_ctgs' : main_ctgs ,
            'sub_ctgs' : sub_ctgs ,
        }
        return render(request,'sub_content.html',context=context)
    else :
        return redirect('index')

def searchPage(request):
    return render(request, 'searchPage.html')

def brandrank(request):
    #브랜드 랭크 페이지
    # - 브랜드 총 조회수 기준, 브랜드 총 like 기준으로 선택정렬
    # - 정렬 옵션 기능(order by query, pg reload)
    # - 스크롤링 기능 미지원    
    # ******************************************
        # brand 총 조회수: brand_view 
        #   // 제품테이블의 브랜드의 조회수 sum
        #   // 나타낼 정보: 제품의 브랜드 이름, 브랜드의 조회수, 조회수 순위

        # 브랜드 총 like: brand_like
        #   // 찜한제품테이블의 브랜드의 좋아요수 sum
        # 
    # ******************************************

    # option: 사용자가누른 옵션(조회수/좋아요)
    option=request.GET.get('option')
    # 먼저 모든 제품 로드
    product=products.objects.all()

    #제품 디테일 페이지 관련
    if request.user.is_authenticated :
        #회원
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
    
    q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)

    # 브랜드를 조회수 기준으로 볼때
    if option=='view':            
        # product[0].Brand.Name_en  >> FCMM //제품의 브랜드 이름
        #   orm_sum쓰는 법: product.aggregate(Sum('origin_price')) >> 제품들의 총 합 나옴        
        #   orm_group_by_sum: product.values('Gender').order_by('Gender').annotate(total=Sum('Origin_price'))   >> Gender별 가격합산 나옴

        # 브랜드별 조회수 딕셔너리 리스트 >> [{'Brand__Name_en': 'Athlete', 'b_v': 335}, {'Brand__Name_en': 'Bunnybugs', 'b_v': 54},...,]
        b_v=product.values('brand__name_en').order_by('brand__name_en').annotate(b_n=Sum('view_count')).order_by('-b_n')
        # 브랜드 리스트
        brand=[]
        # 브랜드별 조회수
        view=[]

        for i in range(0,len(b_v)):
            brand.append(b_v[i]['brand__name_en'])
            view.append(b_v[i]['b_n'])

        context={
            'list':b_v,
            'brand':brand,
            'view':view,
            'gender' : gender ,
            'main_ctgs' : main_ctgs ,
            'sub_ctgs' : sub_ctgs ,
        }

    # 브랜드를 좋아요 기준으로 볼때
    else:
        # 좋아요 테이블 리스트
        p_l=product_likes.objects.values_list('product',flat=True)
        # 브랜드 리스트
        brand=[]
        # 브랜드별 찜한수
        like=[]        
        # 좋아요 테이블의 제품들
        pd=products.objects.filter(pk__in=set(p_l))
        # 좋아요한 테이블 제품들의 브랜드를 그룹화하고 그 수들을 id기준으로 count해준다
        # 아직 좋아요가 없는 브랜드의 경우 count를 해주지 않는다
        b_l=pd.values('brand__name_en').order_by('brand__name_en').annotate(b_n=Count('id')).order_by('-b_n')

        for i in range(0,len(b_l)):
            brand.append(b_l[i]['brand__name_en'])
            like.append(b_l[i]['b_n'])

        context={
            'user':request.user,
            'list':b_l,
            'brand':brand,
            'like':like,
            'gender' : gender ,
            'main_ctgs' : main_ctgs ,
            'sub_ctgs' : sub_ctgs ,
        }
    return render(request,'brandrank.html',context)


def like(request,product_id):
    # 제품을 찜하면 찜하기를 처리하는 controller함수
    # 로그인한 유저만 이 like함수로 처리한다.
    # 로그인하지 않은 유저는 쿠키로 template상에서 저장하기 때문에 이 함수로 들어오지 않는다
    #*****************************************************************

    # DB에 like상품 삽입
    # Product_Likes테이블(p_l)에 사용자(log_user),사용자가 찜한 상품(pd) 삽입하기

    if request.method=="POST":
        try :
            # 테이블에 사용자가 찜한 상품이 이미 들어있을경우 그 내역 삭제
            pd = products.objects.get(id=product_id)
            p_l = product_likes.objects.get(user=request.user,product=pd)
            p_l.delete()
        except products.DoesNotExist:
            #잘못된 상품 요청에 대한 예외처리
            return JsonResponse({'status':0})
        except product_likes.DoesNotExist :
            # 테이블에 사용자가 찜한 상품이 들어있지 않은 경우 삽입
            p_l = product_likes(user=request.user, product=pd)
            p_l.save()
        return JsonResponse({'status': 1})  
    # ajax로` 오는게 실패했을경우
    else:
        # print(request.method)
        # print('로그인 됨_ajax통신 실패...')
        return JsonResponse({'status':0})
        # return 

def likes(request):

    # 하단 메뉴바의 Likes의 내가 좋아요한 상품을 눌렀을 때 나오는 페이지
    #*************************************************************
    # 로그인된 유저일 경우 찜한 목록
    # 쿠키로 저장하여 그 목록들을 보여준다
    if request.user.is_authenticated:
        contents=products.objects.filter(Like_users__user=request.user)
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else:
    # 로그인이 안된 유저일 경우 찜한 목록
    # 각각의 제품을 찜하기를 누를 시 쿠키의 찜한상품들(iteam_array)을 로드한다
        like = request.COOKIES.get('like','')
        like.strip(', ')
        if like != '' :
            like_array=like.split(',')
        # print(like_array)

        try :
            pd_ids = list(map(int, like_array))
            contents = products.objects.filter(id__in=pd_ids)
        except Exception:
            contents = []

        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN

    q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)

    context={
        'gender' : gender,
        'user' : request.user,
        'contents':contents, 
        'main_ctgs' : main_ctgs ,
        'sub_ctgs' : sub_ctgs ,
    }
    return render(request,'likes.html',context)

def best(request):
    #제품 디테일 페이지 관련
    if request.user.is_authenticated :
        #회원
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
    
    q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)    

    p_l=product_likes.objects.values_list('product',flat=True)
    if p_l != '' :
        try:
            pd=products.objects.filter(pk__in=set(p_l))
        except Exception:
            pd=[]

    context={
        'contents':pd,
        'gender' : gender ,
        'main_ctgs' : main_ctgs ,
        'sub_ctgs' : sub_ctgs ,        
        'user' : request.user,
    }

    return render(request,'best.html',context)

# 임의로 50개의 데이터를 수정함. 추후 수정필요
def sale(request):
    #제품 디테일 페이지 관련
    if request.user.is_authenticated :
        #회원
        gender = GenderChar.WOMAN if request.user.gender == GenderType.WOMAN else GenderChar.MAN
        q_gender = Q(gender= request.user.gender)
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
    
    q_gender = Q( gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)    

    contents=products.objects.filter(~Q(discount_rate=0))
    
    context={
        'contents':contents,
        'gender' : gender ,
        'main_ctgs' : main_ctgs ,
        'sub_ctgs' : sub_ctgs ,        
        'user' : request.user,
    }

    return render(request,'sale.html',context)

def nonepg(request):
    print(request)
    return None

#---------------------------------------이하 서비스 시 제거------------------------------------#

# def uploadimg(request):
#     print(request.FILES)
#     if request.method == 'POST' :
#         a = products.objects.get(id = request.POST['prod'])
#         form = UploadImgForm(request.POST, request.FILES)
#         # print(form)
#         if form.is_valid():
#             # handle_uploaded_file(request.FILES['photo'])
#             # a = Img_test(Product=a,Img=request.FILES['photo'])
#             # a.save()
#             return HttpResponse("succeed")
#     return HttpResponse('failed')

# def handle_uploaded_file(f):
#     with open('name.png', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
    
# def test(request):
#     a = request.GET.get('data',-1)
#     try :
#         a = int(a)
#         pd = Products.objects.get(id=a)
#     except ValueError as val_err :
#         return HttpResponse("val err")
#     except Products.DoesNotExist as e :
#         print('Does not exist', a)
#     except Exception as e:
#         print(e)
#     context = {
#         'test' : 'hi'
#     }
#     return render(request,'test.html',context=context)
