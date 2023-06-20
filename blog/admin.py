from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'blog_title', 'blog_slug', 'blog_preview', 'blog_created_at', 'blog_is_publicated', 'blog_views_count'
    )
    list_filter = ('blog_is_publicated',)
    search_fields = ('blog_title', 'blog_created_at',)
