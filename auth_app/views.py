from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def test(request):
    return HttpResponse("ceci n'est pas un format radio !!!!!")
# Create your views here.
