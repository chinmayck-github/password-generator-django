from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    charr=list('abcdefghijklmnopqrstuvwxyz')

    length=int(request.GET.get('length'))

    if(request.GET.get('Uppercase')):
        charr.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if(request.GET.get('Numbers')):
        charr.extend(list('1234567890'))

    if(request.GET.get('Special')):
        charr.extend(list('!@#$%^&*()'))
    
    
    thepassword=''
    for i in range(length):
        thepassword+=random.choice(charr)

    return render(request, 'generator/password.html',{'password':thepassword})


