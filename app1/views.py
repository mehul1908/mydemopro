from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def perm(user):
    return False

def addmember(request):
    return HttpResponse("In add member")

