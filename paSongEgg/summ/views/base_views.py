from django.shortcuts import render, get_object_or_404
from summ.models import News_crawled
from django.core.paginator import Paginator
import news_crawler

def index(request):
   """
   summ 목록 출력
   """
   #입력 파라미터
   page=request.GET.get('page','1')#페이지
   #조회
   question_list=News_crawled.objects.order_by('-title')
   #페이징처리
   paginator=Paginator(question_list,10) #페이지당 10개씩 보여주기
   page_obj=paginator.get_page(page)

   context={'news_list':page_obj}
   return render(request,'summ/news_list.html',context)

def detail(request,news_id):
    """
    summ 내용 출력
    """
    news=get_object_or_404(News_crawled,pk=news_id)
    context={'question':news}
    return render(request,'summ/news_detail.html',context)

def get_data(request):
    """
    크롤링
    """
    news_crawler()
