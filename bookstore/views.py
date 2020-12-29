from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

