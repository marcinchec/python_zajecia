from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("Hello world!")

def parametr(request,param):
    return render(request,'blog/test.html',{'param':param})