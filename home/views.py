from django.shortcuts import render

# Create your views here.from django.shortcuts import render_to_response


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html', {'page_title': 'Home'})


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')
