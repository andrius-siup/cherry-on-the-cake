from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Post, Category
from .forms import PostForm


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
                sortkey = 'lower_name'
                posts = post.annotate(lower_name=Lower('name'))
            # Sort by category name
            if sortkey == 'category':
                sortkey = 'category__name'
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


def add_blog_post(request):
    """ Add a post to the Blog """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_blog_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid!')
    else:
        form = PostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blog_post(request, post_id):
    """ Edit a post in the blog """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog_post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_blog_post(request, post_id):
    """ Delete a post from the blog """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('posts'))
