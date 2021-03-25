from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # always for rendering as we define the templates folder inside our settings page, we should provide the absolute path from tempaltes folder
    return render(request, 'generator/index.html',{"name":"Password Generator"})
    #return HttpResponse('<h2>Welocme to Password Generator</h2>')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thePassword = ''

    length = int(request.GET.get('length',6))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    for x in range(length):
        thePassword += random.choice(characters)



    return render(request, 'generator/password.html', {'password':thePassword})


def about(request):
    return render(request,'generator/about.html')