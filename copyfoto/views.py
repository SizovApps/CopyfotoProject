from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def logSucc(request):
    return render(request, 'logSucc.html')