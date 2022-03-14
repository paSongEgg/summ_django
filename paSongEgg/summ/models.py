from django.contrib.postgres.fields import ArrayField  
from django.db import models

# Create your models here.
# 임시 작성
class NewsTable(models.Model):
    date=models.DateField()
    author=models.TextField()
    title=models.TextField()
    link=models.TextField()
    naver_link=models.TextField()
    content=models.TextField()
    keyword=ArrayField(models.CharField(max_length=100))
