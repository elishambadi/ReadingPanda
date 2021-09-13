from django import forms
from django.db import models
from django.db.models.fields import CharField, TextField
# from django.forms import forms
from django.forms.fields import DecimalField, IntegerField, CharField
from django.forms.widgets import TextInput
from .models import Book


#Simple Book Form

class RawBooksForm(forms.Form):
    title = CharField()
    ISBN = CharField()
    category = CharField()
    rentPrice = DecimalField(decimal_places=2, max_digits=10)
    count = IntegerField()


#  Model form below, directly to the models

class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        
        fields = [
            'title',
            'ISBN',
            'category',
            'rentPrice',
            'count'
        ]

