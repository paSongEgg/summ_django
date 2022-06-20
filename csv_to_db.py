import math
import datetime
import pandas as pd
import os
import django
import warnings
os.environ.setdefault("DJANGO_SETTING_MODULE","paSongEgg.settings")
django.setup()
from summ.models import *

def Run():
    Get_Total("static/new/220620.xlsx")
    Get_Two("static/new/220620_clustering_lv2.xlsx")
    Get_Three("static/new/220620_clustering_lv3.xlsx")
    return

def Get_Total(path):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data=pd.read_excel(path,engine="openpyxl")
        data_frame=data.dropna(how='all')

    for i in range(len(data_frame)):
        dict={}
        date=datetime.datetime.strptime(data_frame['date'][i],'%y-%M-%d')
        dict['date']=datetime.datetime.strftime(date,'%Y-%M-%d')
        dict['press']=data_frame['press'][i]
        #dict['ranking']=data_frame['ranking'][i]
        dict['section']=data_frame['section'][i]
        dict['comment']=data_frame['comment'][i]
        dict['title']=data_frame['title'][i]
        dict['link']=data_frame['link'][i]
        dict['content']=data_frame['content'][i]
        dict['reading']=math.ceil(len(data_frame['content'][i])/750*60)
        dict['keywords']=",".join(list(eval(data_frame['keywords'][i])))
        Total_News(**dict).save()
        key=(Total_News.objects.last())
        dic=eval(data_frame['keywords'][i])
        keyword_list=list(eval(data_frame['keywords'][i]))
        for item in keyword_list:
            dict2={}
            dict2['total']=key
            dict2['section_name']=data_frame['section'][i]
            dict2['keyword']=item
            dict2['score']=dic[item]
            Total_keyword(**dict2).save()

def Get_Two(path):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data=pd.read_excel(path,engine="openpyxl")
        data_frame=data.dropna(how='all')

    for i in range(len(data_frame)):
        dict={}
        dict['cluster_label']=data_frame['cluster_label'][i]
        date=datetime.datetime.strptime(data_frame['date'][i],'%y-%M-%d')
        dict['date']=datetime.datetime.strftime(date,'%Y-%M-%d')
        dict['press']=data_frame['press'][i]
        #dict['ranking']=data_frame['ranking'][i]
        dict['section']=data_frame['section'][i]
        dict['comment']=data_frame['comment'][i]
        dict['title']=data_frame['title'][i]
        dict['link']=data_frame['link'][i]
        dict['content']=data_frame['content'][i]
        dict['reading']=math.ceil(len(data_frame['content'][i])/750*60)
        dict['keywords']=",".join(list(eval(data_frame['keywords'][i])))
        Two_News(**dict).save()
        key=(Two_News.objects.last())
        dic=eval(data_frame['keywords'][i])
        keyword_list=list(eval(data_frame['keywords'][i]))
        for item in keyword_list:
            dict2={}
            dict2['total']=key
            dict2['section_name']=data_frame['section'][i]
            dict2['keyword']=item
            dict2['score']=dic[item]
            Two_keyword(**dict2).save()

def Get_Three(path):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data=pd.read_excel(path,engine="openpyxl")
        data_frame=data.dropna(how='all')

    for i in range(len(data_frame)):
        dict={}
        dict['cluster_label']=data_frame['cluster_label'][i]
        date=datetime.datetime.strptime(data_frame['date'][i],'%y-%M-%d')
        dict['date']=datetime.datetime.strftime(date,'%Y-%M-%d')
        dict['press']=data_frame['press'][i]
        #dict['ranking']=data_frame['ranking'][i]
        dict['section']=data_frame['section'][i]
        dict['comment']=data_frame['comment'][i]
        dict['title']=data_frame['title'][i]
        dict['link']=data_frame['link'][i]
        dict['content']=data_frame['content'][i]
        dict['reading']=math.ceil(len(data_frame['content'][i])/750*60)
        dict['keywords']=",".join(list(eval(data_frame['keywords'][i])))
        Three_News(**dict).save()
        key=(Three_News.objects.last())
        dic=eval(data_frame['keywords'][i])
        keyword_list=list(eval(data_frame['keywords'][i]))
        for item in keyword_list:
            dict2={}
            dict2['total']=key
            dict2['section_name']=data_frame['section'][i]
            dict2['keyword']=item
            dict2['score']=dic[item]
            Three_keyword(**dict2).save()