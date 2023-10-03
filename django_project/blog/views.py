# This has imported render from Django.shortcuts
from django.shortcuts import render
from .models import Post

# Create your views here.

# This is where the logic goes of how we want to create the function that is home page.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})