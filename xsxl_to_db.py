from asyncio.windows_events import NULL
import openpyxl
import os
import django
os.environ.setdefault("DJANGO_SETTING_MODULE","paSongEgg.settings")
django.setup()

from django.shortcuts import redirect
from summ.models import Section_crawled,Section_keyword,Comment_crawled,Comment_keyword,Popular_crawled,Popular_keyword
import string

def Run():
    # popular
    #Get_Popular("static/files")
    # 섹션db 추가
    #Get_Section("static/files")
    #Get_Section("static/files")
    # comment
    Get_Comment("static/files/20220331_언론사별 랭킹뉴스_comment_clustering.xlsx")
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
        dict['reading']=len(row[7].value)//280
        dict['title']=row[5].value
        dict['link']=row[6].value
        dict['content']=row[7].value
        dict['keywords']=row[8].value
        Section_crawled(**dict).save()

        key=Section_crawled.objects.last()
        array=str(row[8].value).strip(string.punctuation).split(',')
        for item in array:
            dict2={}
            dict2['section']=key
            dict2['keyword']=item.strip(string.punctuation)
            dict2['section_name']=row[2].value
            Section_keyword(**dict2).save()

def Get_Popular(path):
    wb2=openpyxl.load_workbook(path)
    sheet12=wb2['Sheet1']
    rows2=sheet12['B2':'I121']

    for row in rows2:
        dict={}
        dict['date']=row[0].value.replace('.','-')
        dict['press']=row[1].value
        dict['ranking']=row[2].value
        if row[3].value=='미제공':
            dict['views']=NULL
        else:
            dict['views']=row[3].value
        dict['reading']=len(row[6].value)//280
        dict['title']=row[4].value
        dict['link']=row[5].value
        dict['content']=row[6].value
        dict['keywords']=row[7].value
        Popular_crawled(**dict).save()

        key=(Popular_crawled.objects.last())
        array=str(row[7].value).strip(string.punctuation).split(',')
        for item in array:
            dict2={}
            dict2['popular']=key
            dict2['keyword']=item.strip(string.punctuation)
            Popular_keyword(**dict2).save()

def Get_Comment(path):
    wb2=openpyxl.load_workbook(path)
    sheet12=wb2['Sheet1']
    rows2=sheet12['B2':'I11']

    for row in rows2:
        dict={}
        dict['date']=row[0].value.replace('.','-')
        dict['press']=row[1].value
        dict['ranking']=row[2].value
        dict['comment']=row[3].value
        dict['reading']=len(row[6].value)//280
        dict['title']=row[4].value
        dict['link']=row[5].value
        dict['content']=row[6].value
        dict['keywords']=row[7].value
        Comment_crawled(**dict).save()

        key=(Comment_crawled.objects.last())
        array=str(row[7].value).strip(string.punctuation).split(',')
        for item in array:
            dict2={}
            dict2['comment']=key
            dict2['keyword']=item.strip(string.punctuation)
            Comment_keyword(**dict2).save()