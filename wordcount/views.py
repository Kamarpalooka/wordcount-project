from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    return render(request, 'count.html', {'fulltext': fulltext, 'wordslist': wordslist, 'wordscount': len(wordslist)})


def about(request):
    return render(request, 'about.html')
