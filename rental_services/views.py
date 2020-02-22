from django.shortcuts import render
from .models import Customer


# Create your views here.
posts = [
    {
        'surname': 'a',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'today'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'tomorrow'
    }
]


def all_customers(request):
    context = {
        # 'posts': Customer.objects.all()
        'posts': posts
    }
    return render(request, 'rental_services/house.html', context)

