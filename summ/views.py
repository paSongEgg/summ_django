from django.db.models import Sum
from django.shortcuts import redirect, render
from summ.models import *
import csv_to_db
from django.db.models import Q
import math

def total(request):
   """
   summ 목록 출력
   """
   number=int(request.GET.get('number','3'))
   if number==1:
       return keyword(request)
   elif number==2:
       return article(request)
   elif number==3:
       return section_three(request)
   else:
       return section_four(request)
# lod 레벨 1
def keyword(request):
    total_keyword_list=list(Total_keyword.objects.values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    world_keyword_list=list(Total_keyword.objects.filter(section_name="세계").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    science_keyword_list=list(Total_keyword.objects.filter(section_name="IT").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    economy_keyword_list=list(Total_keyword.objects.filter(section_name="경제").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    politic_keyword_list=list(Total_keyword.objects.filter(section_name="정치").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    society_keyword_list=list(Total_keyword.objects.filter(section_name="사회").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    life_keyword_list=list(Total_keyword.objects.filter(section_name="생활").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:10])
    context={
        'total_list':total_keyword_list,
        'science_list':science_keyword_list,
        'economy_list':economy_keyword_list,
        'politic_list':politic_keyword_list,
        'society_list':society_keyword_list,
        'life_list':life_keyword_list,
        'economy_list':economy_keyword_list,
        'world_list':world_keyword_list,
        'economy_list':economy_keyword_list,
    }
    return render(request,'summ/level_one.html',context)
# lod 레벨 2
def article(request):
    sort=request.GET.get('sort','comment')#페이지
    order='-'+sort
    news_list=Two_News.objects.order_by(order)[:10]
    for i in news_list:
        i.new_keywords=i.keywords.split(',')
    keyword_list=list(Two_keyword.objects.values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    context={
        'news_list':news_list,
        'keyword_list':keyword_list
    }

    return render(request,'summ/level_two.html',context)
# lod 레벨 3
def section_three(request):
    sort=request.GET.get('sort','comment')#페이지

    world_list=Three_News.objects.filter(section="세계").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in world_list:
        i.new_keywords=i.keywords.split(',')
    science_list=Three_News.objects.filter(section="IT").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in science_list:
        i.new_keywords=i.keywords.split(',')
    economy_list=Three_News.objects.filter(section="경제").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in economy_list:
        i.new_keywords=i.keywords.split(',')
    politic_list=Three_News.objects.filter(section="정치").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in politic_list:
        i.new_keywords=i.keywords.split(',')
    society_list=Three_News.objects.filter(section="사회").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in society_list:
        i.new_keywords=i.keywords.split(',')
    life_list=Three_News.objects.filter(section="생활").annotate(keyword_count=Sum('three_key__score')).order_by('-keyword_count')[:3]
    for i in life_list:
        i.new_keywords=i.keywords.split(',')
    world_keyword_list=list(Three_keyword.objects.filter(section_name="세계").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    science_keyword_list=list(Three_keyword.objects.filter(section_name="IT").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    economy_keyword_list=list(Three_keyword.objects.filter(section_name="경제").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    politic_keyword_list=list(Three_keyword.objects.filter(section_name="정치").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    society_keyword_list=list(Three_keyword.objects.filter(section_name="사회").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    life_keyword_list=list(Three_keyword.objects.filter(section_name="생활").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:3])
    
    context={
        'science_list':science_list,
        'economy_list':economy_list,
        'politic_list':politic_list,
        'society_list':society_list,
        'life_list':life_list,
        'economy_list':economy_list,
        'world_list':world_list,
        'economy_list':economy_list,

        'science_keyword_list':science_keyword_list,
        'economy_keyword_list':economy_keyword_list,
        'politic_keyword_list':politic_keyword_list,
        'society_keyword_list':society_keyword_list,
        'life_keyword_list':life_keyword_list,
        'economy_keyword_list':economy_keyword_list,
        'world_keyword_list':world_keyword_list,
        'economy_keyword_list':economy_keyword_list,
    }
    return render(request,'summ/level_three.html',context)

# lod 레벨 4
def section_four(request):
    sort=request.GET.get('sort','comment')#페이지
    user=request.GET.get('user','30')
    slice=math.floor(int(user)/6)
    world_list=Total_News.objects.filter(section="세계").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in world_list:
        i.new_keywords=i.keywords.split(',')
    science_list=Total_News.objects.filter(section="IT").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in science_list:
        i.new_keywords=i.keywords.split(',')
    economy_list=Total_News.objects.filter(section="경제").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in economy_list:
        i.new_keywords=i.keywords.split(',')
    politic_list=Total_News.objects.filter(section="정치").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in politic_list:
        i.new_keywords=i.keywords.split(',')
    society_list=Total_News.objects.filter(section="사회").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in society_list:
        i.new_keywords=i.keywords.split(',')
    life_list=Total_News.objects.filter(section="생활").annotate(keyword_count=Sum('total_key__score')).order_by('-keyword_count')[:slice]
    for i in life_list:
        i.new_keywords=i.keywords.split(',')
    world_keyword_list=list(Total_keyword.objects.filter(section_name="세계").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    science_keyword_list=list(Total_keyword.objects.filter(section_name="IT").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    economy_keyword_list=list(Total_keyword.objects.filter(section_name="경제").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    politic_keyword_list=list(Total_keyword.objects.filter(section_name="정치").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    society_keyword_list=list(Total_keyword.objects.filter(section_name="사회").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    life_keyword_list=list(Total_keyword.objects.filter(section_name="생활").values('keyword').annotate(keyword_count=Sum('score')).order_by('-keyword_count').distinct()[:5])
    
    context={
        'science_list':science_list,
        'economy_list':economy_list,
        'politic_list':politic_list,
        'society_list':society_list,
        'life_list':life_list,
        'economy_list':economy_list,
        'world_list':world_list,
        'economy_list':economy_list,

        'science_keyword_list':science_keyword_list,
        'economy_keyword_list':economy_keyword_list,
        'politic_keyword_list':politic_keyword_list,
        'society_keyword_list':society_keyword_list,
        'life_keyword_list':life_keyword_list,
        'economy_keyword_list':economy_keyword_list,
        'world_keyword_list':world_keyword_list,
        'economy_keyword_list':economy_keyword_list,
    }
    return render(request,'summ/level_three.html',context)

#db에 저장
def toDB(request):
    csv_to_db.Run()
    return redirect("/")

    