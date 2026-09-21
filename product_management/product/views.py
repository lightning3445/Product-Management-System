from django.shortcuts import render,redirect
from .models import product
from .forms import productform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if request.method=="POST":
        form=productform(request.POST,request.FILES)

        if form.is_valid():
            product_obj=form.save(commit=False)
            product_obj.user=request.user
            product_obj.save()
            return redirect("product_list")

    else:
        form=productform()

    return render(request,"product_form.html",{
        "form":form # takes your Python 
        # form and sends it to the HTML template.
    })

@login_required
def product_list(request):
    products=product.objects.filter(user=request.user)
    search=request.GET.get("search")

    if search:
        products=product.objects.filter(name__icontains=search)

    return render(request,"product_list.html",{
        "products":products,
        "search":search
    })

@login_required
def product_detail(request,proid):
    products=product.objects.get(proid=proid,user=request.user)

    return render(request,"product_detail.html",{
        "products":products
    })

@login_required
def edit_product(request,proid):
    product_obj=product.objects.get(proid=proid,user=request.user)

    if request.method=="POST":

        form=productform(request.POST,request.FILES,instance=product_obj)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form=productform(instance=product_obj)

    return render(request,"product_form.html",{
        "form":form
    })

# instance=product_obj tells Django:
# Update this existing product instead of 
# creating a new product.

@login_required
def delete_product(request,proid):
    product_obj=product.objects.get(proid=proid)
    product_obj.delete()

    return redirect("product_list")

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect('product_list')

    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

#  render means take that html file and show it to the user

# _______________________________________________

# product_obj = form.save(commit=False)
# means:
# Create the product object, but don't save it yet.

# product_obj.user = request.user
# means:
# This product belongs to the currently logged-in user.

# product.objects.filter(user=request.user)
# means:
# Only give me products belonging to the currently logged-in user.