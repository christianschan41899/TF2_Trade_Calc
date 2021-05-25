from django.shortcuts import render, redirect

# Create your views here.

def AboutPage(request):
    return render(request, 'about.html')
