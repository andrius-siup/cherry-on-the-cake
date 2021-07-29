from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<post_id>/', views.blog_post_detail, name='blog_post_detail'),
]
