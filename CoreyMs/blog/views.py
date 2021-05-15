from django.shortcuts import render

# Create your views here.


posts = [
    {'author': 'prateek',
     'title': 'My First Blog Post',
     'content': 'First Post Content',
     'date_posted': 'May 2,2021'

     },
    {'author': 'zubin',
     'title': 'My second Blog Post',
     'content': 'second  Post Content',
     'date_posted': 'May 3,2021'

     }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
