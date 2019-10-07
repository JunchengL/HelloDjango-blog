from django.shortcuts import render

from django.http import HttpResponse
 
def index(request):
    return render(request, 'blog/index.html', context={
        'title': "JCC's Blog",
        'welcome': 'Welcome to my Blog'
    })