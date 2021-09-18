from django.shortcuts import render

# Create your views here.
def index(request):
    pass
    return render(request, 'posts/index.html',)    


def about(request):
    pass
    return render(request, 'posts/about.html',)


def contact(request):
    pass
    return render(request, 'posts/contact.html',)


def post(request):
    pass
    return render(request, 'posts/post.html',)