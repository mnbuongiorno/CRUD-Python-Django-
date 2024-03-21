from django.shortcuts import render, redirect
from store.models import Product
from django.contrib import messages

def home(request):
    return render(request,"principal.html")

def consult(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products' : products
    })
    
def save_products(request):
    name = request.POST["name"]
    price = request.POST["price"]
    description = request.POST["description"]
    p = Product(name=name, price=price, description=description)
    p.save()
    messages.success(request,'Added product')
    return redirect('consult')

def delete(request, id):
    product = Product.objects.filter(pk=id)
    product.delete()
    messages.success(request, 'Deleted product')
    return redirect('consult')

def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request,"editProduct.html", {
        'product' : product
    })
    
def edit(request):
    if request.method == 'POST':
        id = request.POST["id"]
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            messages.error(request, 'Product not found')
            return redirect('consult') 

        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        product.save()
        messages.success(request, 'Updated product')
        return redirect('consult')
