from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    capital= string.ascii_uppercase
    numbers= '0123456789'
    chars = "!@#$%^&*()"
    length = int(request.GET.get('length'))
    initial = string.ascii_lowercase
    final = ''
    if request.GET.get('Capital'):
        initial= initial + capital
    if request.GET.get('Numbers'):
        initial = initial + numbers
    if request.GET.get('Chars'):
        initial = initial + chars
    for i in range(length):
        final += random.choice(initial)
    return render(request, 'generator/password.html', {'password':final})



    return render(request, 'generator/password.html')

