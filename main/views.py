from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Shop(request):
    return render(request,'shop.html')

def About(request):
    
    return render(request,'about.html')

def Service(request):
    
    return render(request,'service.html')

def Blog(request):
    
    return render(request,'blog.html')

def contract(request):
    return render(request,'contact.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def Cart(request):
    return render(request,'cart.html')