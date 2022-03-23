from django.urls import path
from .views import base_views

app_name='summ'

urlpatterns = [
    # base_views.py
    path('',base_views.index, name='index'),
    path('crawl',base_views.get_data),
    path('<int:news>', base_views.detail, name='detail'),
]