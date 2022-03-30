from asyncio.windows_events import NULL
from django.shortcuts import redirect
import openpyxl
import os
import django
os.environ.setdefault("DJANGO_SETTING_MODULE","paSongEgg.settings")
django.setup()

from django.shortcuts import redirect
from summ.models import Section_crawled,Section_keyword,Comment_crawled,Comment_keyword,Popular_crawled,Popular_keyword
import string
def Run():
    # 섹션db 추가
    wb=openpyxl.load_workbook('static/files/20220330_정치_20.xlsx')
    sheet1=wb['Sheet1']
    rows=sheet1['C2':'K11']

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
            Section_keyword(**dict2).save()
    # comment
    wb2=openpyxl.load_workbook('static/files/20220327_언론사별 랭킹뉴스_20.xlsx')
    sheet12=wb2['Sheet1']
    rows2=sheet12['B2':'I11']

    for row in rows2:
        dict={}
        dict['date']=row[0].value.replace('.','-')
        dict['press']=row[1].value
        dict['ranking']=row[2].value
        dict['comment']=row[3].value
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
    return