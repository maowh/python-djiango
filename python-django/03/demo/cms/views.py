from django.shortcuts import render

# Create your views here.


def cms(request):
    return render(request, "cms.html")
