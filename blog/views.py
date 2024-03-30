from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        "author": "Saurav Navdhare",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "March 31, 2024"
    },
    {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "April 01, 2024"
    }
]


def home(Request):
    context = {
        "posts": posts\
    }
    # return HttpResponse("<h1>Home Page</h1>")
    return render(Request, 'blog/home.html', context)

def about(Request):
    # return HttpResponse("<h1>Blog Page</h1>")
    return render(Request, 'blog/about.html', {'title': 'About Page'})