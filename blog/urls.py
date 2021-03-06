from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_blog_post'),
    path('add_comment/<int:post_id>/', views.add_post_comment, name='add_post_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_post_comment, name='delete_post_comment'),
]
