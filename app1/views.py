from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
def perm(user):
    return False
# @permission_required('perm' , login_url='app2:login')
def addmember(request):
    return HttpResponse("In add member")

