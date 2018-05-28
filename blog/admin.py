from django.contrib import admin

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Required', {'fields': ['title', 'author', 'text']}),
        ('Attributes', {'fields': ['tags', 'image_url']}),
        ('When to publish', {'fields': ['publication_date']}),
    ]
 #   inlines = [TagInline]
    list_display = ('title', 'author', 'is_published', 'publication_date')
    list_filter = ['publication_date', 'author', 'tags']
    search_fields = ['title', 'author', 'text']


class TagAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        needed to hide model from admin page
        """
        return {}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
