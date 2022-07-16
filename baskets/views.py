from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from baskets.models import Basket
from mainapp.models import Product


def basket_add(requets, id):
    user_select = requets.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=user_select, product=product)

    if baskets:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)
    return HttpResponseRedirect(requets.META.get('HTTP_REFERER'))


def basket_remove(requets, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(requets.META.get('HTTP_REFERER'))
