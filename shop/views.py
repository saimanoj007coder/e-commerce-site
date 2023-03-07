from django.shortcuts import render
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    product=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":product})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})

def register(request):
    return render(request,"shop/register.html")

def collectionsview(request,name):
 if (Catagory.objects.filter(name=name,status=0)):
    product=Product.objects.filter(category__name=name)
    return render(request,"shop/products/index.html",{"products":product,"category_name":name})
 else:
    messages.warning(request,"no category found")
    return redirect("collections")

def productdetails(request,cname,pname):
 if (Catagory.objects.filter(name=cname,status=0)):
    if (Product.objects.filter(name=pname,status=0)):
     product=Product.objects.filter(name=pname,status=0).first()
     return render(request,"shop/products/productdetail.html",{"products":product,"category_name":cname,"product_name":pname})
    else:
     messages.warning(request,"no product found")
     return redirect("collections")
 else: 
    messages.warning(request,"no category found")
    return redirect("collections")