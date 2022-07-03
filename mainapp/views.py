# Представления(контроллеры), они импортируются в urls, и описывают действия, при их вызове чере urls
# В нашем случае они рендерят(отображают) страницу

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Soapshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Soapshop - Каталог',
    }
    return render(request, 'mainapp/products.html', context)
