from django.shortcuts import render
from .models import Post


def blogs(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, "blog/blogs.html", context)
