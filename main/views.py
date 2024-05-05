from django.shortcuts import render,redirect
from.form import *
from .models import*
from django.views import View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, reverse
from django.db.models import Q
from django.db.models import F
from django.http import JsonResponse
from django.db.models import Sum
from django.http import HttpResponseBadRequest
# Create your views here.
def Home(request):
    product_home=Product.objects.all()[:3]
    
    
    return render(request,'index.html',locals())
class ProductDetailsview(View):
    def get(self,request,pk):
        
        product_detail=Product.objects.get(pk=pk)
        
        return render(request,'product_details.html',locals())
    
def carts(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        product_quantity = request.GET.get('product_quantity')
        product = Product.objects.get(id=product_id)
        try:
            cart_item = Cart.objects.get(user=user, product=product)
            quantity = cart_item.quantity
            cart_item.quantity = product_quantity
            cart_item.save()
            #cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user,product=product,quantity=product_quantity)
            cart.save()
        return redirect('/cart')
       
def show_cart(request):
    
    if request.user.is_authenticated:

        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                temamount=(p.quantity*p.product.price)
                amount=temamount+amount
                
            
            return render(request,"cart.html",{'cart':cart,'line_total':Cart.line_total,'amount':amount})
                           
        else:
            
            return render(request,'404.html')
        

def plus_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        cart = Cart.objects.get(id=cart_id, user=request.user)
        cart.quantity = F('quantity') + 1
        cart.save(update_fields=['quantity'])
        
        return JsonResponse({
            "status": "success",
            "cart_id": cart_id,
            "quantity": cart.quantity,
            "line_total": cart.line_total(),
            "cart_total": Cart.objects.filter(user=request.user).aggregate(cart_total=Sum('line_total'))['cart_total']
        })

def minus_cart(request):
    if request.method == 'GET':
        cart_id = request.GET['cart_id']
        cart = Cart.objects.get(id=cart_id, user=request.user)
        if cart.quantity <= 1:
            cart.quantity = 1
        else:
            cart.quantity = F('quantity') - 1
        cart.save(update_fields=['quantity'])
        
        return JsonResponse({
            "status": "success",
            "cart_id": cart_id,
            "quantity": cart.quantity,
            "line_total": cart.line_total(),
            "cart_total": Cart.objects.filter(user=request.user).aggregate(cart_total=Sum('line_total'))['cart_total']
        })
def Shop(request):
    shop_item=Product.objects.all()[3:]
    
    return render(request,'shop.html',locals())

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

