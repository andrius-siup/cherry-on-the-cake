from django.contrib import admin
from .models import Post, Category, BlogPostComment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_by',
        'date',
    )

    ordering = ('-date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class BlogPostCommentAdmin(admin.ModelAdmin):
    fields = (
        'post', 'name', 'email', 'content', 'date',
    )

    readonly_fields = (
        'name', 'email', 'content', 'date',
    )

    list_display = (
        'post',
        'name',
        'email',
        'content',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPostComment, BlogPostCommentAdmin)
