from django.shortcuts import render, redirect
from .models import *
from .myforms import *


def index(req):
    return render(req, 'index.html')


def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    p1 = Product(name='orange', price=140)
    p2 = Product(name='multy', price=150)
    p3 = Product(name='apple', price=160)
    c1 = Company.objects.get(title='J7')
    c2 = Company.objects.get(title='DOBRY')
    # c2.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c2.product_set.add(p3, bulk=False)
    print(c2.product_set.count())
    print(c2.product_set.values())
    print(c2.product_set.values_list())
    return redirect('index')


def table1(req):
    baza = Product.objects.all()
    anketa = FormJuice()
    print(Company.objects.values_list('title', flat=False))
    bd = []
    for i in baza:
        bd.append((i.name, i.price, i.firma.title))
    title = ('Название', 'Цена', 'Фирма')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)