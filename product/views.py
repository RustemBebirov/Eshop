from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from .forms import SearchForm
from django.contrib import messages
import json


def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)

    context = {
        'product': product
    }

    return render(request,'product-page.html',context)


def category_product(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id).all()
    context = {
        'category':category,
        'products':products
    }
    return render(request,'products.html',context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            categories = Category.objects.all()
            search = form.cleaned_data['search']
            
            products = Product.objects.filter(title__icontains=search).all()
                
            context = {
                            'products':products,
                            'category':categories
                        }
                
            if not products:
                messages.warning(request, 'Products not found')
                return render(request,'products_search.html',context)
            return render(request,'products_search.html',context)
    return HttpResponseRedirect('/')

def product_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        products = Product.objects.filter(title__icontains=q)
        results = []
        for product in products:
            product_json = {}
            product_json = product.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
        