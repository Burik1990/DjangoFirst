from django.shortcuts import render

from catalog.models import Product, Category


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) : {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категория товара'
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/product.html', context)
