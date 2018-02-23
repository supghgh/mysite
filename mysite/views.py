from django.http import HttpResponse

def index(request):
    return HttpResponse('<H2>Hey!</H2>')
