from django.urls import path
from .views import product_list, product_detail, category_list, homepage,add_to_cart,view_cart,checkout

urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', product_list, name='product_list'),
    path('products/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('categories/', category_list, name='category_list'),
    path('cart/', view_cart, name='view_cart'),
    path('add_to_cart/<int:id>/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
]
