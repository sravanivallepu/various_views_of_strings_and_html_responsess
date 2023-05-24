from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def firststring(request):
    return HttpResponse('<marquee><h1>This is our first view http response in the form of string</h1></marquee>')
def secondstring(request):
    return HttpResponse('<marquee><i>This is our second view http response in the form of string</i></marquee>')
def firstpage(request):
    return render(request,'firstpage.html')
def secondpage(request):
    return render(request,'secondpage.html')
