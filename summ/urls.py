from django.urls import path
from . import views

app_name='summ'

urlpatterns = [
    # base_views.py
    path('',views.total, name='total'),
    path('db',views.toDB,name="toDB"),
]