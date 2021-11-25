from django.contrib import admin
from blog.models import Blog
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'added_date', 'updated_date', 'is_published']
    list_per_page = 25
    search_fields = ['title', 'content']
    ordering = ['title', '-updated_date']
    list_filter = ['is_published']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Blog, BlogAdmin)
