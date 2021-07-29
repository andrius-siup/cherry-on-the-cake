from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category


def posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey ='lower_name'
                posts = post.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = posts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('posts'))

            queries = Q(title__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
