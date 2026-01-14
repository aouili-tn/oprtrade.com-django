from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    """Home page view with hero section"""
    return render(request, 'website/home.html')

def about(request):
    """About Us page view"""
    return render(request, 'website/about.html')

def contact(request):
    """Contact Us page view with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        company = request.POST.get('company', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # In a production environment, you would:
        # 1. Validate the data
        # 2. Save to database or send email
        # 3. Redirect to success page
        
        # For now, just show a success message
        messages.success(request, f'Thank you {name}! Your message has been received. We will contact you soon at {email}.')
    
    return render(request, 'website/contact.html')

