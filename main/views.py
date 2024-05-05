from django.shortcuts import render,redirect
from.form import *
from .models import*
from django.views import View
from django.contrib import messages
# Create your views here.
def Home(request):
    product_home=Product.objects.all()[:3]
    
    
    return render(request,'index.html',locals())
class ProductDetailsview(View):
    def get(self,request):
        
        return render(request,'product_details.html')
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
    
    form=RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulation Succesfully Registration Done')
            return redirect('login')
        
        else:
            return render(request,'eror.html')
        
            
    
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def Cart(request):
    return render(request,'cart.html')