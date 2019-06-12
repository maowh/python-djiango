from django.shortcuts import render


class Person(object):
    def __init__(self, username):
        self.username = username


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
