from django.shortcuts import render, redirect, reverse
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
    if request.method == 'GET':
        return render(request, "add_book.html")
    else:
        name = request.POST.get("name")
        cursor = get_cursor()
        cursor.execute("insert into collage(id,name) values(null,'%s')" % name)
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select * from collage where id=%s" % book_id)
    collage = cursor.fetchone()
    return render(request, 'book_detail.html', context={"collage": collage})


def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        print(book_id)
        cursor = get_cursor()
        cursor.execute("delete from collage where id=%s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除学院错误")


def modify_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book_name = request.POST.get("book_name")
        cursor = get_cursor()
        cursor.execute("update collage set name='%s' where id=%s" % (book_name, book_id))
        return redirect(reverse('index'))
    else:
        raise RuntimeError("修改学院错误")


