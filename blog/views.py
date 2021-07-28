from django.shortcuts import render

# Create your views here.
def blogs(request):
    """ A view to show all blog posts """
    return render(request, "blog/blogs.html", )
