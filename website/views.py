from django.shortcuts import render
from django.contrib import messages
from .models import ContactPage


def home(request):
    context = {
        'title': 'Gewa Wallet'
    }
    return render(request, 'website/home.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'website/about.html', context)

def contact(request):
    context = {
        'title': 'Contact Us'
    }
    if request.method == 'POST':
        contact = ContactPage.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            message = request.POST.get('message')
        )
        contact.save()
        messages.success(request, 'Your message has been delivered')
    return render(request, 'website/contact_form.html', context)

def handler404(request, exception):
    return render(request, 'website/error_404.html')

def handler500(request):
    return render(request, 'website/error_500.html')