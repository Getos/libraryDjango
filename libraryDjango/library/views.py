from django.shortcuts import render
from .models import Book


def posts_list(request):
    books = Book.objects.all()
    return render(request, 'posts/posts_list.html', {'books': books})
# Create your views here.
