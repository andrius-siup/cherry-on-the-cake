from django.shortcuts import render


def blogs(request):
    """ A view to show all blog posts """
    return render(request, "blog/blogs.html", )
