from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Post


def posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('posts'))

            queries = Q(title__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(queries)

    context = {
        'posts': posts,
        'search_term': query,
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
