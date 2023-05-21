from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def list_view(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,"product/list.html",context)

def details(request,pk):
    product=Product.objects.get(id=pk)
    context={
        'product':product
    }
    return render(request,"product/detials.html",context)

def create(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        'form':form
    }
    return render(request,"product/create.html",context)

def update(request,pk):
    product=Product.objects.get(id=pk)
    form=ProductForm(request.POST or None,instance=product)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        'form':form
    }
    return render(request,"product/create.html",context)

def delete(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=="POST":
            product.delete()
            return redirect("/")
    return render(request,"product/delete.html")
    