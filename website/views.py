from django.shortcuts import render

# Create your views here.

def home(request):
    """Home page view with hero section"""
    return render(request, 'website/home.html')

def about(request):
    """About Us page view"""
    return render(request, 'website/about.html')

def contact(request):
    """Contact Us page view"""
    return render(request, 'website/contact.html')

