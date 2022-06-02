from asyncio.windows_events import NULL
import openpyxl
import os
import django
os.environ.setdefault("DJANGO_SETTING_MODULE","paSongEgg.settings")
django.setup()
import math
from django.shortcuts import redirect
from summ.models import Total_News,Total_keyword,Section_crawled,Section_keyword
import string

def Run():
    # popular
    #Get_Popular("static/files")
    # 섹션db 추가
    #Get_Section("static/files")
    #Get_Section("static/files")
    # comment
    Get_Total("static/new/전체_clustering.xlsx")
    return
def Get_Section(path):
    wb=openpyxl.load_workbook(path)
    sheet1=wb['Sheet1']
    rows=sheet1['B2':'J19']

    for row in rows:
        dict={}
        dict['date']=row[0].value.replace('.','-')
        dict['press']=row[1].value
        dict['section']=row[2].value
        dict['ranking']=row[3].value
        if row[4].value=='미제공':
            dict['views']=NULL
        else:
            dict['views']=row[4].value
        dict['reading']=round(len(row[7].value)/750)
        dict['title']=row[5].value
        dict['link']=row[6].value
        dict['content']=row[7].value
        dict['keywords']=row[8].value.strip('[]')
        Section_crawled(**dict).save()

        key=Section_crawled.objects.last()
        array=str(row[8].value).strip(string.punctuation).split(',')
        for item in array:
            dict2={}
            dict2['section']=key
            dict2['keyword']=item.strip(string.punctuation)
            dict2['section_name']=row[2].value
            Section_keyword(**dict2).save()

def Get_Total(path):
    wb2=openpyxl.load_workbook(path)
    sheet12=wb2['Sheet1']
    rows2=sheet12['B2':'K51']

    for row in rows2:
        dict={}
        dict['cluster_label']=row[0].value
        dict['date']=row[1].value
        dict['press']=row[2].value
        #dict['ranking']=row[2].value
        dict['section']=row[4].value
        dict['comment']=row[5].value
        dict['reading']=math.ceil(len(row[9].value)/750)
        dict['title']=row[6].value
        dict['link']=row[7].value
        dict['content']=row[8].value
        dict['keywords']=row[9].value.strip('[]')
        print("..saving")
        Total_News(**dict).save()
        print("saved!")
        key=(Total_News.objects.last())
        array=str(row[9].value).strip(string.punctuation).split(',')
        for item in array:
            dict2={}
            dict2['total']=key
            dict2['keyword']=item.strip(string.punctuation)
            Total_keyword(**dict2).save()

