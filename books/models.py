from django.db import models
from django.db.models.fields import CharField, DecimalField, IntegerField

# Create your models here.
class Book(models.Model):
    title = CharField("bookTitle", max_length=120)
    ISBN = CharField("ISBN", max_length=100, unique=True)
    category = CharField("category", max_length=100)
    count = IntegerField("count")
    rentPrice = DecimalField("rentPrice",  max_digits=20, decimal_places=2)

