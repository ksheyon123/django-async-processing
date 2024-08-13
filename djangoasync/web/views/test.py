from django.http import HttpResponse

from django.shortcuts import render
from djangoasync.tasks import add

def renderer(request):
    result = add(1, 1)
    print(result)
    context = {
        "add" : result
    }
    return render(request, 'test.html', context)