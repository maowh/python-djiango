from django.shortcuts import render
from django.db import connection

# Create your views here.


def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute("select * from collage")
    collages = cursor.fetchall()
    return render(request, "index.html", context={'collages': collages})


def add_book(request):
    pass


def book_detail(request, book_id):
    pass

