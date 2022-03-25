from django.contrib import admin
from .models import News_crawled,News_keyword

class News_Admin(admin.ModelAdmin):
    search_fields=['title']

class News_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

admin.site.register(News_crawled,News_Admin)
admin.site.register(News_keyword,News_keyword_Admin)