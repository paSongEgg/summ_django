from django.contrib import admin
from .models import Section_crawled, Comment_crawled,Popular_crawled,Popular_keyword,Comment_keyword,Section_keyword

class Section_Admin(admin.ModelAdmin):
    search_fields=['section']

class Comment_Admin(admin.ModelAdmin):
    search_fields=['title']

class Popular_Admin(admin.ModelAdmin):
    search_fields=['title']

class Popular_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

class Comment_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

class Section_keyword_Admin(admin.ModelAdmin):
    search_fields=['section']

admin.site.register(Section_crawled,Section_Admin)
admin.site.register(Comment_crawled,Comment_Admin)
admin.site.register(Popular_crawled,Popular_Admin)
admin.site.register(Section_keyword,Section_Admin)
admin.site.register(Comment_keyword,Comment_Admin)
admin.site.register(Popular_keyword,Popular_Admin)