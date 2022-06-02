from django.db import models

# Create your models here.
class Total_News(models.Model):
    id=models.BigAutoField(primary_key=True)
    cluster_label=models.IntegerField(null=True)
    comment=models.IntegerField(null=True)
    content=models.TextField(null=True)
    date=models.DateField(null=True)
    keywords=models.CharField(max_length=150,null=True)
    link=models.CharField(max_length=400,null=True)
    press=models.CharField(max_length=20,null=True)
    reading=models.IntegerField(null=True)
    section=models.CharField(max_length=10,null=True)
    title=models.CharField(max_length=200,null=True) 

    def __str__(self):
        return self.title

class Total_keyword(models.Model):
    id = models.BigAutoField( primary_key=True)
    total=models.ForeignKey("Total_News",on_delete=models.CASCADE,null=True)
    section_name=models.CharField(max_length=20,null=True)
    keyword=models.CharField(max_length=20,null=True)
    score=models.FloatField(null=True)
