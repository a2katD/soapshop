# Представления(контроллеры), они импортируются в urls, и описывают действия, при их вызове чере urls
# В нашем случае они рендерят(отображают) страницу

import json
import os

from django.shortcuts import render

from mainapp.models import Products, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'Soapshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Soapshop - Каталог',
    }
    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Products.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)
