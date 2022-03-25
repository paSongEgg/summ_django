from django.contrib import admin
from django.urls import path,include
from summ.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summ/',include('summ.urls')),
    path('', base_views.index, name='index'),
]

