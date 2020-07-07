from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from datetime import datetime
from .models import products


def Home(request):
    allproducts = products.objects.all()
    date_now = datetime.date(datetime.now())
    template = loader.get_template('index.html')
    context = {
        'ap': allproducts,
        'date': date_now,
    }
    return HttpResponse(template.render(context, request))


def product(request, product_id):
    item = None
    product = products.objects.all()
    for i in product:
        if i.id == product_id:
            item = i
    return render(request, 'details.html', {'item': item})
