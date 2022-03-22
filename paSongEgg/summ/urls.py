from django.urls import path
from .views import base_views

app_name='summ'

urlpatterns = [
    # base_views.py
    path('',base_views.index, name='index'),
    path('<int:question_id>', base_views.detail, name='detail'),
]