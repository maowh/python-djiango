from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


class Person(object):
    def __init__(self, username):
        self.username = username


def greet():
    return "hello!"


def index(request):
    # p = Person("赵六")
    # context = {
    #     'person': p
    # }
    # context = {
    #     'person': {
    #         'username': '赵六'
    #     }
    # }

    context = {
        'persons': [
            '鲁班一号',
            '鲁班二号',
            '鲁班三号'
        ],
        'greet': greet,
        'book': {
            'bookid': 1,
            'bookname': '三国演义',
            'bookauthor': '赵六'
        },
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 97
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 76
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 89
            }
        ],
        'comments': []
    }
    # context = {
    #     'age': 18
    # }
    return render(request, "index.html", context=context)


def company(request):
    return render(request, "company.html")


def school(request):
    return render(request, "school.html")


def add_view(request):
    # context = {
    #     'value1': [1, 2, 3],
    #     'value2': [5, 6, 7]
    # }
    context = {
        'today': datetime.now()
    }
    return render(request, "add.html", context=context)


def login(request):
    next = request.GET.get('next')
    text = '登录页面，登录完成后要跳转的url是：%s' % next
    return HttpResponse(text)


def book(request):
    return HttpResponse("读书页面")


def book_detail(request, book_id, category):
    text = "您的图书id是 %s，图书分类是 %s" % (book_id, category)
    return HttpResponse(text)


def movie(request):
    return HttpResponse("电影页面")


