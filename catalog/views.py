from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(requests):
    return render(requests, 'contacts.html')