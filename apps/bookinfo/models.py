from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from apps.users.models import Account


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class DisCount(models.Model):
    name_of_book = models.CharField(max_length=30)
    new_price = models.IntegerField()

    def __str__(self):
        return self.name_of_book


class BookInfo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    discount = models.ForeignKey(DisCount, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = RichTextField()
    on_sale = models.BooleanField(default=False)
    isbn = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=20, null=True)
    type_of_lang = models.CharField(max_length=20, null=True)
    translator = models.CharField(max_length=20, null=True)
    num_of_pages = models.IntegerField(null=True)
    press = models.CharField(max_length=20, null=True)
    publish_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BookImage(models.Model):
    book_info = models.ForeignKey(BookInfo, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return f'Image of {self.book_info}'


class Rate(models.Model):
    RATE = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    book_info = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE, default=0)

    def __str__(self):
        return self.user.email
