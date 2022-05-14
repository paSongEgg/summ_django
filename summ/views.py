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
   sort=request.GET.get('sort','views')#페이지
   slice=int(request.GET.get('number','5'))
   if slice==0:
       return keyword(request)
   #조회
   order='-'+sort
   news_list=slicing(slice,Popular_crawled,order)
   context={'news_list':news_list}
   return render(request,'summ/news_list.html',context)

def slicing(val,data,order):
    if val==5:
        return data.objects.order_by(order)
    else:
        newSlice=10*val
        return data.objects.order_by(order)[:newSlice]
    

def section(request):
    #입력 파라미터
    sort=request.GET.get('sort','views')#페이지
    theme=request.GET.get('theme','경제')
    print(theme)
    order='-'+sort
    slice=int(request.GET.get('number','5'))
    if slice==0:
        return keyword(request)
    elif slice==5:
        if theme=="IT":
            news_list=list(Section_crawled.objects.filter(Q(section=theme)|Q(section="과학")).order_by(order).values())
        elif theme=="생활":
            news_list=list(Section_crawled.objects.filter(Q(section=theme)|Q(section="문화")).order_by(order).values())
        else:
            news_list=Section_crawled.objects.filter(section=theme).order_by(order)
    else:
        slice=slice*10
        if theme=="IT":
            news_list=list(Section_crawled.objects.filter(Q(section=theme)|Q(section="과학")).order_by(order)[:slice].values())
        elif theme=="생활":
            news_list=list(Section_crawled.objects.filter(Q(section=theme)|Q(section="문화")).order_by(order)[:slice].values())
        else:
            news_list=Section_crawled.objects.filter(section=theme).order_by(order)[:slice]

    #조회
    context={'news_list':news_list}
    return render(request,'summ/section_list.html',context)


def toDB(request):
    xsxl_to_db.Run()
    return redirect("/")

def comment(request):
   #입력 파라미터
   sort=request.GET.get('sort','comment')#페이지
   slice=request.GET.get('number','전체')
   if slice=='키워드':
        return keyword(request)
   #조회
   if sort=="views" :
       sort='comment'
   order='-'+sort
   news_list=slicing(slice,Comment_crawled,request,order)
   context={'news_list':news_list}
   return render(request,'summ/comment_list.html',context)

def keyword(request):
    #section
    world_keyword_list=list(Section_keyword.objects.filter(section_name="세계").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    science_keyword_list=list(Section_keyword.objects.filter(section_name="IT").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    economy_keyword_list=list(Section_keyword.objects.filter(section_name="경제").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    politic_keyword_list=list(Section_keyword.objects.filter(section_name="정치").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    society_keyword_list=list(Section_keyword.objects.filter(section_name="사회").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    life_keyword_list=list(Section_keyword.objects.filter(section_name="생활").values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    #comment
    com_keyword_list=list(Comment_keyword.objects.values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    #popular
    pop_keyword_list=list(Popular_keyword.objects.values('keyword').annotate(keyword_count=Count('keyword')).order_by('-keyword_count').values())
    context={
        'science_list':science_keyword_list,
        'economy_list':economy_keyword_list,
        'politic_list':politic_keyword_list,
        'society_list':society_keyword_list,
        'life_list':life_keyword_list,
        'world_list':world_keyword_list,
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
    