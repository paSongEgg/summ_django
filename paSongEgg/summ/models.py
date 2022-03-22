from django.db import models

# Create your models here.
class News_crawled(models.Model):
    data=models.JSONField()    


