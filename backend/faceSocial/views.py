from django.shortcuts import render

def home(request):
    return render(request, 'faceSocial/index.html')

def messages(request):
    return render(request, 'faceSocial/messages.html')
