from books.models import Book
from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Book
from books.forms import BookModelForm, RawBooksForm


# Create your views here.

def books_list_view(request):
    all_books = Book.objects.all()
    print(all_books)

    context = {
        "books" : all_books
    }

    return render(request, "books/list.html", context)

def books_create_view(request):
    # if request.method == "POST":
    #     print(request.POST.get("book-title"))

    form = RawBooksForm()
    if request.method == "POST":
        book_form = BookModelForm(request.POST or None)
        if book_form.is_valid():
            book_form.save()
        # book_form.save() ONLY FOR MODEL FORMS

        # if book_form.is_valid:
        #     print(book_form.cleaned_data)
        #     Book.objects.create(**book_form.cleaned_data) #** is to present the data as arguments

    context = {
            "form":form
    }

    return render(request, "books/create.html", context)

def books_find_view(request, id):
    book = Book.objects.get(id=1)

    context = {
        "one_book":book
    }

    return render(request, "books/detail.html", context)