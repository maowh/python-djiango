from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    cursor.execute("select * from machine")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')
