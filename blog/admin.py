from django.contrib import admin
from .models import Post, Category


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


admin.site.register(Post, PostAdmin)  # PostAdmin
admin.site.register(Category, CategoryAdmin)  # CategoryAdmin
