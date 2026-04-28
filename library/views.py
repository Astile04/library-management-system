from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Member

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})  

def author_list(request):
    authors = Author.objects.all().order_by('name')
    return render(request, 'library/author_list.html', {'authors': authors})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})
