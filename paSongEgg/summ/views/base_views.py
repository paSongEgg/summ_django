from django.shortcuts import render, get_object_or_404
from summ.models import Popular_crawled,Comment_crawled,Section_crawled
from django.core.paginator import Paginator
import news_crawler

def index(request):
   """
   summ 목록 출력
   """
   #입력 파라미터
   # page=request.GET.get('page','1')#페이지
   #조회
   news_list=Popular_crawled.objects.order_by('-views')
   #페이징처리

   context={'news_list':news_list}
   return render(request,'summ/news_list.html',context)

def detail(request,news_id):
    """
    summ 내용 출력
    """
    news=get_object_or_404(Popular_crawled,pk=news_id)
    context={'news':news}
    return render(request,'summ/news_detail.html',context)

def section(request):
    #입력 파라미터
    #page=request.GET.get('page','1')#페이지
    #조회
    news_list=Section_crawled.objects.order_by('-date')

    context={'news_list':news_list}
    return render(request,'summ/section_list.html',context)

def get_data(request):
    """
    크롤링
    """
    news_crawler.main(request)
