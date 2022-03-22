from django.contrib import admin
from .models import News_crawled

class News_Admin(admin.ModelAdmin):
    search_fields=['title']

admin.site.register(News_crawled,News_Admin)