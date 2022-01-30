from itertools import product
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from.models import *
from django.db.models import *
# Create your views here.
from django.shortcuts import render
from .models import *
from django.views import View
def home(request):
    bottomwears = Product.objects.filter(category='BW')
    context = {
        'bottomwears':bottomwears,
      
       
    }
    return render(request, 'store/store.html',context)

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.all(),

        bottomwears = Product.objects.filter(category='BW'),
        mobiles = Product.objects.filter(category='M'),
        return render(request,'store/store.html',{'topwears':topwears,'bottomwears':bottomwears})

# def product_detail(request,pk):

#  return render(request, 'store/product-detail.html')
class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk) 
        item_in_cart = False
        item_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'store/product-detail.html',{'product':product,'item':item_in_cart})

def add_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart/')
    
def category_list(request):
    data = Category.objects.all()
    return render(request,'store/category-list.html',{'data':data})
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data = Product.objects.filter(title__icontains=q)
        
    else:
        data = Product.objects.all()
    context = {
		'data':data
	}
    return render(request,'store/search.html',context)
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount =30
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for k in cart_product:
                # tempamount = (k.quantity * k.product.price)
                # amount += tempamount
                total_amount = amount  + shipping_amount
        return render(request,'store/cart.html',{'carts':cart,'total_amount':total_amount})
    else:
        return render(request,'store/emptycart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def remove_cart(request,pk=None):
    Cart.objects.get(id=pk).delete()
    return redirect('cart')


def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):

    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'iphone' or 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    else:
        mobiles = []
    context = {
        'mobiles':mobiles
    }
    return render(request, 'store/mobile.html',context)

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
    user = request.user
    item = Cart.objects.filter(user=user)
    add = Customer.objects.filter(user=user)
    context = {
        'item':add,
        'items':item
           
        }
    return render(request, 'store/checkout.html',context)

# def home(request):
#     product = Product.objects.all()
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer,complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#     context = {
#         'product':product,
#          'order':order
#     }
#     return render(request,'store/store.html',context)
# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer,complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
        
#     context = {
#            'items':items,
#            'order':order,
#         }
#     return render(request,'store/cart.html',context)
# def checkout(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer,complete=False)
    #     items = order.orderitem_set.all()
    # else:
    #     items = []
        
    # context = {
    #        'items':items,
    #        'order':order,
    #     }
#     return render(request,'store/checkout.html',context)
# def product_detail(request,pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'product':product
#     }
    
#     return render(request, 'store/product-detail.html',context)
# def add_to_cart(request):
#     user = request.user
#     product_id = request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     OrderItem(user=user,product=product).save()
#     return redirect('/carts')
    
# def show_cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         cart = OrderItem.objects.filter(user=user)
#         return render(request,'store/cart.html',{'carts':cart})

# def updateitem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action',action)
#     print('Product',productId)

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer,complete=False)

#     orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

#     if action == 'add':
#         orderItem.quantity  = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity  = (orderItem.quantity - 1)
#     orderItem.save()
#     return JsonResponse('item was added',safe=False)
