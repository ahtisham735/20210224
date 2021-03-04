from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"singlePage1/index.html")
def section(request,num):
    text=["Section1","Section2","Section3"]
    return HttpResponse(text[num-1])