from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.
def front(request):
    ## 将html渲染为python字符串
    # html = render_to_string("index.html")
    # # 包装为httpresponse对象返回
    # return HttpResponse(html)
    return render(request, "front.html")


