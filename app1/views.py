from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_String(request):
    return HttpResponse('<h1> This is the First app1_String</h1> ')

def app1_HTML(request):
    return render(request,'app1_HTML.html')