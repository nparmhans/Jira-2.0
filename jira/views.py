from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'GET':
        return render(request, 'jira/home.html')
    else:
        return HttpResponse("Not Home Page")


def not_found(request):
    return render(request, 'jira/404.html')


def server_error(request):
    return render(request, 'jira/500.html')
