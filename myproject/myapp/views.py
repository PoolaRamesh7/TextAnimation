from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    mydict = {'name':"hello how are you"}
    return render(request,'home.html',context=mydict)

def smoke(request):
    return render(request, 'smokename.html',)

def SME(request):
    name1 = request.GET['name']
    return render(request, 'SME.html',{'Name': name1})

def Reflection(request):
    return render (request, 'reflection.html',)

def Reflectioneffect(request):
    name1 = request.GET['name']
    return render(request, 'reflectioneffect.html',{'Name': name1})

def Background(request):
    return render (request, 'background.html',)

def Backgroundeffect(request):
    name1 = request.GET['name']
    return render(request, 'Backgroundeffect.html',{'Name': name1})

def Fire(request):
    return render (request, 'fireb.html',)

def FireBEffect(request):
    name1 = request.GET['name']
    return render(request, 'FireBEffect.html',{'Name': name1})
