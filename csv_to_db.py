import math
import datetime
import pandas as pd
import os
import django
import warnings
os.environ.setdefault("DJANGO_SETTING_MODULE","paSongEgg.settings")
django.setup()
from summ.models import Total_News,Total_keyword

def Run():
    Get_Total("static/new/전체_clustering.xlsx")
    return

def Get_Total(path):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        data_frame=pd.read_excel(path,engine="openpyxl")
        data=data_frame.dropna(how='all')

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
        dict['reading']=math.ceil(data_frame['comment'][i]/750)
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