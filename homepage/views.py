from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def about_us(request):
    return render(request, 'footer/about_us.html')

def careers(request):
    return render(request, 'footer/careers.html')

def stories(request):
    return render(request, 'footer/stories.html')

def return_policy(request):
    return render(request, 'footer/return_policy.html')

def terms_of_use(request):
    return render(request, 'footer/terms_of_use.html')

def privacy(request):
    return render(request, 'footer/privacy.html')