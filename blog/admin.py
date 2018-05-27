from django.contrib import admin

from .models import Post, Tag

# Register your models here.


# class TagInline(admin.TabularInline):
#   model = Tag
#  extra = 2

#class TagInline(admin.TabularInline):
#    model = Tag.



class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Required', {'fields': ['title', 'author', 'text']}),
        ('Attributes', {'fields': ['tags', 'image_url']}),
        ('When to publish', {'fields': ['publication_date']}),
    ]
 #   inlines = [TagInline]
    list_display = ('title', 'author', 'is_published')
    list_filter = ['publication_date', 'author', 'tags']
    search_fields = ['title', 'author', 'text']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)