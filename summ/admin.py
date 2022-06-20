from django.contrib import admin
from .models import Total_News,Total_keyword,Three_News,Three_keyword,Two_News,Two_keyword

class Total_Admin(admin.ModelAdmin):
    search_fields=['title']

class Total_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

class Two_Admin(admin.ModelAdmin):
    search_fields=['title']

class Two_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

class Three_Admin(admin.ModelAdmin):
    search_fields=['title']

class Three_keyword_Admin(admin.ModelAdmin):
    search_fields=['keyword']

admin.site.register(Total_News,Total_Admin)
admin.site.register(Total_keyword,Total_keyword_Admin)
admin.site.register(Two_News,Two_Admin)
admin.site.register(Two_keyword,Two_keyword_Admin)
admin.site.register(Three_News,Three_Admin)
admin.site.register(Three_keyword,Total_keyword_Admin)