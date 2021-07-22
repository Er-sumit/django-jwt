from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home page. We'll have interactive homepage soon. <br></br>"
        + "<a href='/admin'>Click here</a> to go to Administrative activities <br></br>"
        + "<a href='/auth'>Click here</a> to go to Authentication Application <br></br>"
        )