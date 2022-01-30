from django.urls import  path 
from .import views
from .import *


urlpatterns =[
    path('',views.home,name='store'),
    path('cart/',views.show_cart,name='cart'),
    path('search',views.search,name='search'),
    path('category/',views.category_list,name='category-list'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),
    path('mobile',views.mobile,name='mobile'),
    # path('carts/',views.profile,name='show-cart'),
    path('add-cart/',views.add_cart,name='add-cart'),
    # path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('delete-homework/<int:pk>/',views.remove_cart,name='remove-cart'),
    
    # path('update_item/',views.updateitem,name='update_item'),
]