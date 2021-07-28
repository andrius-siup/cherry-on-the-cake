from django.contrib import admin
from .models import Post, Category


# class PostAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'content',
#         'created_date',
#         'created_by',
#     )

#     ordering = ('created_date')


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'name'
#     )


admin.site.register(Post)  # PostAdmin
admin.site.register(Category)  # CategoryAdmin
