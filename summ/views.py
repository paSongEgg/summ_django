from django.db.models import Count
from django.shortcuts import redirect, render, get_object_or_404
from summ.models import Comment_crawled,Section_crawled, Section_keyword,Comment_keyword,Popular_crawled,Popular_keyword
import news_crawler
import xsxl_to_db
from django.db.models import Q


def index(request):
   """
   summ 목록 출력
   """
   #입력 파라미터
   sort=request.GET.get('sort','comment')#페이지
   slice=int(request.GET.get('number','100'))
   if slice==10:
        return keyword(request)
   #조회
   order='-'+sort
   news_list=Comment_crawled.objects.order_by(order)[:slice]
   context={'news_list':news_list}
   return render(request,'summ/news_list.html',context)

def section(request):
    #입력 파라미터
    sort=request.GET.get('sort','views')#페이지
    theme=request.GET.get('theme','정치')
    print(type(theme))
    if theme=="IT":
        print(theme)
    elif theme=="생활":
        print(theme)
    order='-'+sort
    slice=int(request.GET.get('number','100'))
    if slice==10:
        return keyword(request)

    #조회
    news_list=Section_crawled.objects.filter(section=theme).order_by(order)[:slice]
    context={'news_list':news_list}
    return render(request,'summ/section_list.html',context)


def toDB(request):
    xsxl_to_db.Run()
    return redirect("/")

def popular(request):
   """
   summ 목록 출력
   """
   #입력 파라미터
   sort=request.GET.get('sort','comment')#페이지
   slice=int(request.GET.get('number','100'))
   if slice==10:
        return keyword(request)
   #조회
   order='-'+sort
   news_list=Popular_crawled.objects.order_by(order)[:slice]
   context={'news_list':news_list}
   return render(request,'summ/news_list.html',context)

def keyword(request):
    #조회
    '''sec_duplicates = Section_keyword.objects.values('keyword').annotate(keyword_count=Count('keyword'))
    sec_keyword_list=Section_keyword.objects.filter(
        cnt__in=[item['keyword'] for item in sec_duplicates]
    ).order_by('cnt')
    com_duplicates = Comment_keyword.objects.values('keyword').annotate(cnt=Count('keyword'))
    com_keyword_list=Comment_keyword.objects.filter(
        cnt__in=[item['keyword'] for item in com_duplicates]
    ).order_by('cnt')
    pop_duplicates = Popular_keyword.objects.values('keyword').annotate(cnt=Count('keyword'))
    pop_keyword_list=Popular_keyword.objects.filter(
        cnt__in=[item['keyword'] for item in pop_duplicates]
    ).order_by('cnt')'''
    sec_keyword_list=Section_keyword.objects.values('keyword').annotate(total=Count('keyword')).order_by('total')
    com_keyword_list=Comment_keyword.objects.values('keyword').annotate(total=Count('keyword')).order_by('total')
    pop_keyword_list=Comment_keyword.objects.values('keyword').annotate(total=Count('keyword')).order_by('total')
    context={
        'sec_list':sec_keyword_list,
        'com_list':com_keyword_list,
        'pop_list':pop_keyword_list,
    }
    return render(request,'summ/keyword_list.html',context)

def get_data(request):
    """
    크롤링
    """
    news_crawler.main()
    return redirect("/")
    