from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def homepage(request):
    # categories = Category.objects.all()
    # featured_products = Product.objects.filter(avaliable=True)[:5]  # Adjust the number of featured products as needed

    # context = {
    #     'categories': categories,
    #     'featured_products': featured_products,
    # }
    return render(request, 'home.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avaliable=True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category.html', context)





from django.shortcuts import render

def view_cart(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'cart.html', context)

def add_to_cart(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart
    return redirect('view_cart') 


def checkout(request):
    # Implement your checkout logic here
    return render(request, 'checkout.html')  # Assuming you have a 'checkout.html' template

