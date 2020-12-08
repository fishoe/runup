from django.shortcuts import render, redirect
from .models import SubCategories, MainCategories, Brands, Products, Users, Similarities
from .models import Review_rates, Reviews, Product_Likes, Scatch_result
from .models import Main_banner 
from .forms import UploadImgForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.http import Http404, HttpResponseNotFound

from config.settings import DEBUG
if DEBUG == True : 
    from .models import Img_test, Img_temp
    from django.http import HttpResponse

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
    q_common = Q(Gender = CtgGenderType.COMMON)
    q_ngen = Q(Gender = CtgGenderType.NONE)

    main_ctgs = MainCategories.objects.filter( q_gender | q_ngen | q_common).order_by('pk')
    sub_ctgs = SubCategories.objects.filter(q_gender | q_common | q_ngen ).order_by('Main')

    return main_ctgs,sub_ctgs

def main(request):

    #로그인 인증
    if request.user.is_authenticated :
        #회원 메뉴 아이템
        #회원 성별 획득
        user = request.user
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
    
    flt_opt = request.GET.get('flt','?')
    all_pd = Products.objects.filter(q_gender | Q( Gender=GenderType.COMMON )).order_by(flt_opt)#정렬 옵션에 대한 것
    prod_page = Paginator(all_pd, const.ITEMS_PER_PAGE ) #모든 상품을 30개 보여준다.
    page = prod_page.get_page(1)

    main_ctgs, sub_ctgs = GetCtg(q_gender)

    #메인 포스트 노출 파트

    active_banner_list = Main_banner.objects.filter( Q(Start__gte = timezone.now())| Q(End__lte = timezone.now()) )

    context = {
        'contents' : page, #상품 목록 리스트 Products
        'gender' : gender, #사용자 성별
        'main_post' : active_banner_list, #현재 표시 되는 배너 리스트 쿼리 리스트 Main_banner
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'login' : request.user.is_authenticated,
        'user_data' : request.user, #유저 메뉴 리스트
    }

    res = render( request, 'main_content.html', context)
    
    #cookie save if user is authenticated
    if request.user.is_authenticated is False : 
        res.set_cookie('gender', gender )
    return res

def category_pg(request):
    #auth
    if request.user.is_authenticated :
        #회원
        pass
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
    try :
        sub_ctg_id = int(request.GET.get('s_ctg',-1))
        flt = request.GET.get('flt','?')
        if sub_ctg_id == -1 :
            main_ctg_id = int(request.GET.get('m_ctg',-1))
            main_ctg = MainCategories.objects.get(id = main_ctg_id)
            sub_ctg = None
            ctg_pd_list = Products.objects.filter( Category__Main=main_ctg_id ).order_by(flt) 
        else :
            sub_ctg = SubCategories.objects.get( id = sub_ctg_id )
            if sub_ctg.Gender != CtgGenderType.COMMON and sub_ctg.Gender != CtgGenderType.NONE:
                gender = GenderChar.WOMAN if sub_ctg.Gender == CtgGenderType.WOMAN else GenderChar.MAN
            main_ctg = sub_ctg.Main
            ctg_pd_list = Products.objects.filter( Category=sub_ctg ).order_by(flt) #todo
        paginator = Paginator(ctg_pd_list, const.ITEMS_PER_PAGE )
        page = paginator.get_page(1)
    except ValueError as e:
        raise Http404('invalid value')
    except MainCategories.DoesNotExist as e :
        raise Http404('not m_ctg')
    except SubCategories.DoesNotExist as e :
        raise Http404('not s_ctg')

    q_gender = Q( Gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)

    #print(request.user)

    context = {
        'contents' : page , #상품 목록 리스트 Products
        'm_ctg': main_ctg ,
        's_ctg' : sub_ctg ,
        's_ctg_friends' : main_ctg.sub_ctgs.all(), #현 카테고리 메인의 친구들
        'gender' : gender, #사용자 성별
        'main_ctgs' : main_ctgs, #메인 카테고리 리스트 
        'sub_ctgs' : sub_ctgs, #서브 카테고리 리스트
        'user_data' : request.user, #유저 메뉴 리스트
    }
    if request.is_ajax():
        ctg_page = int(request.GET.get('page',-1))
        context['contents']=paginator.page(ctg_page)
        return render(request,'ctg_content.html',context=context)
    else :
        return render(request,'ctg_content.html', context=context )

def product_pg(request, product_id):
    try :
        pd = Products.objects.get( id=product_id )
    except Products.DoesNotExist as e:
        raise Http404(e)
    contents = Similarities.objects.filter(Target_prod=pd).order_by('-Sim_val') 

    #리프레시 검사(리프레시를 이용한 뷰카운트 조작 방지 구현)
    pd.View_count += 1

    #제품 디테일 페이지 관련
    if request.user.is_authenticated :
        #회원
        pass
    else :
        #비회원
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN
        if pd.Gender != GenderType.COMMON :
            gender = GenderChar.WOMAN if pd.Gender == GenderType.WOMAN else GenderChar.MAN
    
    q_gender = Q( Gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
    main_ctgs, sub_ctgs = GetCtg(q_gender)

    context = {
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

def styleCatch(request):
    if request.user.is_authenticated :
        return render(request, 'styleCatch.html')
    else :
        return render(request, 'styleCatch.html')

from django.views.decorators.csrf import csrf_exempt, csrf_protect

def analyzing(request):
    if request.user.is_authenticated is False and request.method == 'POST': 
        #회원 구현이 아직 되지 않아서 임시로 넣었습니다.
        #구현이 되면 is False를 제거해서 씁시다.
        
        #성별을 가져옵니다. 지금은 쿠키를 쓰겟습니다.
        gender = request.COOKIES['gender'] if 'gender' in request.COOKIES else GenderChar.WOMAN

        # print(request.FILES)
        #request의 포스트 데이터의 validate 체크
        form = UploadImgForm(request.POST, request.FILES)
        if form.is_valid() :
            img = request.FILES['photo'] if 'photo' in request.FILES else request.FILES['album']
            s_result = Img_temp(Img=img)
            s_result.save()
        else :
            return HttpResponseNotFound("Not valid Image")
        #대충 알고리즘을 돌렸습니다
        class ACLS():
            pass
        main = ACLS()
        main.Img_url = s_result.Img.url 

        q_gender = Q( Gender = GenderType.WOMAN if gender == GenderChar.WOMAN else GenderType.MAN )
        main_ctgs, sub_ctgs = GetCtg(q_gender)
        smpl_pd = Products.objects.all().order_by('?')[0]
        contents = smpl_pd.Target_prod.all().order_by('-Sim_val')

        context = {
            'main' : main ,
            'contents' : contents ,
            'gender' : gender ,
            'main_ctgs' : main_ctgs ,
            'sub_ctgs' : sub_ctgs ,
        }
        return render(request,'sub_content.html',context=context)
    else :
        return redirect('index')

def recommend(request):
    #auth 확인 후 로그인 페이지 리다이렉트
    #파일 읽기 후 페이지에서 리사이징 js 이용
    #파일 업로드 후 추천 시스템 모듈 이용
    #결과 값을 통한 제품 추천 페이지 이동
    return None

def searchPage(request):
    return render(request, 'searchPage.html')

#---------------------------------------이하 서비스 시 제거------------------------------------#

def nonepg(request):
    print(request)
    return None

def uploadimg(request):
    print(request.FILES)
    if request.method == 'POST' :
        a = Products.objects.get(id = request.POST['prod'])
        form = UploadImgForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['photo'])
            # a = Img_test(Product=a,Img=request.FILES['photo'])
            # a.save()
            return HttpResponse("succeed")
    return HttpResponse('failed')

def handle_uploaded_file(f):
    with open('name.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
def test(request):
    a = request.GET.get('data',-1)
    try :
        a = int(a)
        pd = Products.objects.get(id=a)
    except ValueError as val_err :
        return HttpResponse("val err")
    except Products.DoesNotExist as e :
        print('Does not exist', a)
    except Exception as e:
        print(e)
    context = {
        'test' : 'hi'
    }
    return render(request,'test.html',context=context)