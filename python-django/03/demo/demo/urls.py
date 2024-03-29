"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front import views_front
from cms import views as views_cms
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('movie/', views.movie, name='movie'),
    path('book/detail/<book_id>/<category>/', views.book_detail, name='book_detail'),
    path('login/', views.login, name='login'),
    path('add/', views.add_view, name='add'),
    path('school/', views.school, name='school'),
    path('company/', views.company, name='company'),
    path('admin/', admin.site.urls),
    path('front/', views_front.front, name='front'),
    path('cms/', views_cms.cms, name='cms')
]
