from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def faq(request):
    return render(
        request,
        'single_pages/faq.html'
    )
