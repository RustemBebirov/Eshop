from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

from .models import ShopCart
from .forms import ShopCartForm




@login_required(login_url='/user/login')
def shopcart(request):
    cart_products = ShopCart.objects.filter(user=request.user)
    total = 0
    for product in cart_products:
        total += product.product.price * product.qty
    context = {
        'cart_products':cart_products,
        'total':total,
    }

    return render(request,'cart.html',context)



@login_required(login_url='/user/login')
def addtocart(request,id):
    current_user= request.user
    print(current_user)
    url = request.META.get('HTTP_REFERER')
    check = ShopCart.objects.filter(product=id,user=current_user).first()

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if check:
                check.qty += form.cleaned_data['qty']
                check.save()
            else:

                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.qty = form.cleaned_data['qty']
                data.save()

        request.session['cart_items']= ShopCart.objects.filter(user=current_user).count()
        messages.success(request,'Product add to cart')
        return HttpResponseRedirect(url)
    if id:
        if check:
            check.qty += 1
            check.save()
        else:

            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.qty = 1
            data.save()

        messages.success(request,'Product add to cart')

        return HttpResponseRedirect(url)
    request.session['cart_items']= ShopCart.objects.filter(user=current_user).count()
    messages.warning(request,'product not add')
    return HttpResponseRedirect(url)


@login_required(login_url='/user/login')
def deletetocart(request,id):
    ShopCart.objects.get(id=id).delete()
    request.session['cart_items']= ShopCart.objects.filter(user=request.user).count()
    messages.success(request,'Product successfuly delete')
    return redirect(reverse_lazy('order:shopcart'))