from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the auth index, we'll begin authentication shortly")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)