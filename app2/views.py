from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_String(request):
    return HttpResponse('<h1> This is the app2_String response</h1>')
def app2_HTML(request):
    return render(request,'app2_HTML.html')