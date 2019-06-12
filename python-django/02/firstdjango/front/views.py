from django.shortcuts import render
from django.http import HttpResponse
# redirect重定向路由，reverse路由反转解析路由名
from django.shortcuts import redirect, reverse


# Create your views here.
def index(request):
    # 判断用户名是否存在，存在则到前台首页，否则到登录页面
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页！')
    else:
      #  return redirect('/login/')
      return redirect(reverse('front:login'))


def login(request):
    return HttpResponse('前台登录页面！')

