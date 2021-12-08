from django.http import HttpResponse
import logging

def index(request):
    return HttpResponse('<H2>Hey!</H2>')
