from django.shortcuts import render
import random 
#from typing import List
# Create your views here.

def about(request):
    """Funcion que retorna el about de la pagina"""
    return render(request,'generator/about.html')

def home(request):
    """Nos dirige al archivo home"""
    return render(request,'generator/home.html')

def password(request):
    """Esta ruta toma los datos dentro de request con los que genera una contraseña.
    Return:
        Retorna el render de passwords.html con los datos que se pasan como argumento"""
    #Leer los datos de request
    length = int(request.GET.get('length'))
    #status_uppercase = request.GET.get('uppercase')

    #Generando la contraseña
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    generated_password = ''
    
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!¿{*[/]#}&¡'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    #
    for x in range(length):
        generated_password += random.choice(characters)
    
    #
    return render(request,'generator/password.html',{'password':generated_password})