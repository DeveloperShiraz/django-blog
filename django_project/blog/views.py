# This has imported render from Django.shortcuts
from django.shortcuts import render
from django.http import HttpResponse  # This is for Http

# Create your views here.


# This is where the logic goes of how we want to create the function that is home page.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')