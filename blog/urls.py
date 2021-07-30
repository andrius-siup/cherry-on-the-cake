from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
]
