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
    readonly_fields = ['added_date', 'updated_date']
    date_hierarchy = 'updated_date'
    actions = ('make_published',)
    # fields = (
    #     ('added_date','updated_date'),
    #     ('title','slug'),
    #     'content'
    #     )
    fieldsets = (
        (None, {'fields': (('added_date', 'updated_date'),),
         'description': 'Time Information'}),
        ('Must Properties', {'fields': ('title', 'content'),
         'description': 'The object has to have these attributes'}),
        ('Nice to Have Properties', {'fields': (('slug', 'is_published'),),
         'description': 'If the object hasn\'t these attributes, they will be automatically generated'})
    )

    def make_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f"{count} objects changed")

    make_published.short_description = 'Publish The Selected Blogs'


admin.site.register(Blog, BlogAdmin)
