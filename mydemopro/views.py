from django.http import HttpResponse , request

def hello(req):
    return HttpResponse("Welcome to django project")