from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = "магазин"
    products = Product.objects.all()
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = "Контакты"
    contacts_list = [
        {'town': 'Москва', 'phone': '8-999-777-77-77', 'email': 'moscow@yandex.ru', 'address': 'Проспект Мира 41'},
        {'town': 'Казань', 'phone': '8-888-666-66-66', 'email': 'kazand@yandex.ru', 'address': 'Ленина 20'},
        {'town': 'Питер', 'phone': '8-777-555-55-55', 'email': 'piter@yandex.ru', 'address': 'Петергоф  1'},
    ]

    context = {
        'title': title,
        'contacts_list': contacts_list
    }
    return render(request, 'geekshop/contact.html', context=context)
