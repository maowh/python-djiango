from django.urls import path
from . import views

# 应用命名空间的变量app_name
app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]
