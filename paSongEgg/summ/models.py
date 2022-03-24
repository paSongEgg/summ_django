from django.db import models

# Create your models here.
class News_crawled(models.Model):
    date=models.DateField(null=True)
    press=models.CharField(max_length=15,null=True)
    title=models.CharField(max_length=200,null=True)
    link=models.CharField(max_length=400,null=True)
    content=models.TextField(null=True)
    ranking=models.IntegerField(null=True)
    views=models.IntegerField(null=True)

    #data=JSONField()    
    def __str___(self):
        return self.title


class News_keyword(models.Model):
    news_id=models.ForeignKey("News_crawled", on_delete=models.CASCADE,db_column="news")
    keyword=models.CharField(max_length=20,null=True)
