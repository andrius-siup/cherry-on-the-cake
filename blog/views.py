from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, "blog/blogs.html", context)


def blog_post_detail(request, post_id):
    """ A view to show individual blog post details """
    global post
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, "blog/blog-post-detail.html", context)
