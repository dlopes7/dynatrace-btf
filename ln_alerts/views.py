from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bt_feed(request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse('Request Processed')
    else:
        return HttpResponse('Only POST')
