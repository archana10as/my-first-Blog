from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def archana(request):
    return HttpResponse("Hello, world. archana polls index.")
# Create your views here.
