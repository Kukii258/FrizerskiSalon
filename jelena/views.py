# Create your views here.
from django.shortcuts import render


def naslovnica(request):
    return render(request, "html/index.html")
