from django.db import models

# Create your models here.
class Popular_crawled(models.Model):
    date=models.DateField(null=True)
    press=models.CharField(max_length=15,null=True)
    ranking=models.IntegerField(null=True)
    views=models.IntegerField(null=True)
    title=models.CharField(max_length=200,null=True)
    link=models.CharField(max_length=400,null=True)
    content=models.TextField(null=True)
    keywords=models.CharField(max_length=150,null=True)

    #data=JSONField()    
    def __str___(self):
        return self.title
# Create your models here.
class Comment_crawled(models.Model):
    date=models.DateField(null=True)
    press=models.CharField(max_length=15,null=True)
    ranking=models.IntegerField(null=True)
    comment=models.IntegerField(null=True)
    title=models.CharField(max_length=200,null=True)
    link=models.CharField(max_length=400,null=True)
    content=models.TextField(null=True)
    keywords=models.CharField(max_length=150,null=True)

    #data=JSONField()    
    def __str___(self):
        return self.title
# Create your models here.
class Section_crawled(models.Model):
    date=models.DateField(null=True)
    press=models.CharField(max_length=15,null=True)
    section=models.CharField(max_length=10,null=True)
    ranking=models.IntegerField(null=True)
    views=models.IntegerField(null=True)
    title=models.CharField(max_length=200,null=True)
    link=models.CharField(max_length=400,null=True)
    content=models.TextField(null=True)
    keywords=models.CharField(max_length=150,null=True)

    #data=JSONField()    
    def __str___(self):
        return self.title

class Popular_keyword(models.Model):
    news_id=models.ForeignKey("Popular_crawled", on_delete=models.CASCADE,db_column="news")
    keyword=models.CharField(max_length=20,null=True)

class Comment_keyword(models.Model):
    news_id=models.ForeignKey("Popular_crawled", on_delete=models.CASCADE,db_column="news")
    keyword=models.CharField(max_length=20,null=True)

class Section_keyword(models.Model):
    news_id=models.ForeignKey("Popular_crawled", on_delete=models.CASCADE,db_column="news")
    keyword=models.CharField(max_length=20,null=True)
