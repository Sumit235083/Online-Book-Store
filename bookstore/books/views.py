from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q
from collections import defaultdict

# 🏠 Home Page - Show all books
def home(request):
    query = request.GET.get('q')
    books = Book.objects.all()

    # SEARCH MODE
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__icontains=query)
        )

        return render(request, 'books/home.html', {
            'books': books,
            'query': query
        })

    # CATEGORY GROUPING MODE
    grouped = defaultdict(list)

    for book in books:
        grouped[book.category].append(book)

    category_books = [
        {
            'category': category,
            'books': books_list
        }
        for category, books_list in grouped.items()
    ]

    return render(request, 'books/home.html', {
        'category_books': category_books,
        'query': None
    })


# 📖 Book Detail Page
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    # Optional: show related books (same category)
    related_books = Book.objects.filter(category=book.category).exclude(id=book.id)[:4]

    context = {
        'book': book,
        'related_books': related_books
    }
    return render(request, 'books/book_detail.html', context)


# 📚 Category Page
def category_view(request, category):
    books = Book.objects.filter(category=category)

    context = {
        'books': books,
        'category': category
    }
    return render(request, 'books/category.html', context)


# 🔍 Search Functionality
def search(request):
    query = request.GET.get('q')

    results = Book.objects.all()

    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__icontains=query)
        )

    context = {
        'books': results,
        'query': query
    }
    return render(request, 'books/search.html', context)