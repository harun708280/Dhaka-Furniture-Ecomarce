from django.urls import path
from.import views
from .form import *
from django.contrib.auth import login,logout
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='home'),
    path('shop,',views.Shop,name='shop'),
    path('about/',views.About,name='about'),
    path('service/',views.Service,name='service'),
    path('blog/',views.Blogs,name='blog'),
    path('contact',views.contract,name='contact'),
    
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('log-out/',auth_views.LogoutView.as_view(next_page='login'),name='log-out'),
    path('registration/',views.registration,name='registration'),
    path('add-to-cart/',views.carts,name='add-to-cart'),
    path('cart/',views.show_cart,name='cart'),
    path('product_details/<int:pk>/',views.ProductDetailsview.as_view(),name='product_details'),
    path('plus_cart',views.plus_cart,name="plus_cart"),
    path('minas_cart',views.minus_cart,name="minas_cart"),
    path('delete_carts/<int:id>/',views.Delete_cart,name='delete_carts'),
    path('chackout/',views.Checkout,name='chackout'),
    path('orderplace/',views.order_place,name='order_now'),
    path('order_succes/',views.order_succes,name='order_succes'),
    path('order-details/',views.order_details,name='order-details'),
    path('order_delete/<int:id>/',views.order_delate,name='order-delete'),
    path('no-ordar/',views.noorder_page,name='no-order')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
