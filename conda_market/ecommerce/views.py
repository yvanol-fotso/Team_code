from django.shortcuts import render,get_object_or_404, redirect


# Create your views here.


def home(request):
   
    return render(request, 'home/index.html')


def product(request):
   
    return render(request, 'home/product.html')


def about(request):
   
    return render(request, 'home/about.html')


def contact(request):
   
    return render(request, 'home/contact.html')
