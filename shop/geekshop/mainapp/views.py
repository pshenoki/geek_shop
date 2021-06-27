from django.shortcuts import render

from mainapp.models import MenuCategory


def products(request):
    title = "продукты/каталог"
    links_menu = MenuCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request=request, template_name='mainapp/products.html', context=context)
