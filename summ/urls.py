from django.urls import path
from . import views

app_name='summ'

urlpatterns = [
    # base_views.py
    path('',views.index, name='index'),
    path('sections',views.section,name='section'),
    path('comment',views.comment,name='comment'),
    path('crawl',views.get_data,name='create_data'),
    path('db',views.toDB,name="toDB"),
]