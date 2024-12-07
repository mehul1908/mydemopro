from django.urls import path
from . import views

app_name='app1'

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
urlpatterns = [
    path('',views.addmember),
    path('hello' , views.addmember )
]