# Представления(контроллеры), они импортируются в urls, и описывают действия, при их вызове чере urls
# В нашем случае они рендерят(отображают) страницу

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')
