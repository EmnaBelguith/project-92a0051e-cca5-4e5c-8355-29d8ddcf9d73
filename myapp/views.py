# myapp/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django! This is a minimal test project.")