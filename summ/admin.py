from django.contrib import admin
from .models import Total_News,Total_keyword

class Total_Admin(admin.ModelAdmin):
    search_fields=['title']

class Total_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']


admin.site.register(Total_News,Total_Admin)
admin.site.register(Total_keyword,Total_keyword_Admin)