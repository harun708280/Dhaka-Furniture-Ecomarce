from django.urls import path
from.import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('shop,',views.Shop,name='shop'),
    path('about/',views.About,name='about'),
    path('service/',views.Service,name='service'),
    path('blog/',views.Blog,name='blog'),
    path('contact',views.contract,name='contact'),
    
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('cart/',views.Cart,name='cart')
]
