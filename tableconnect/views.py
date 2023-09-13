from django.shortcuts import render, redirect
from .models import *
from .myforms import *


def index(req):
    return render(req, 'index.html')


def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    # p1 = Product(name='orange', price=140)
    # p2 = Product(name='multy', price=150)
    # p3 = Product(name='apple', price=160)
    # c1 = Company.objects.get(title='J7')
    # c2 = Company.objects.get(title='DOBRY')
    # c2.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c2.product_set.add(p3, bulk=False)
    # print(c2.product_set.count())
    # print(c2.product_set.values())
    # print(c2.product_set.values_list())

    # s1 = Student.objects.create(name='Viktor', group='G001')
    # s2 = Student.objects.create(name='Igor', group='G001')
    # s3 = Student.objects.create(name='Alex', group='G001')
    # s4 = Student.objects.create(name='Zahar', group='G002')
    # s5 = Student.objects.create(name='Andrey', group='G002')
    # k1 = Course.objects.create(title='Math')
    # k2 = Course.objects.create(title='Geo')
    # k1.student_set.add(s1, s3, s5)
    # k2.student_set.add(s1, s2, s3)
    return redirect('index')


def table1(req):
    baza = Product.objects.all()
    anketa = FormJuice()
    bd = []
    if req.POST:
        anketa = FormJuice(req.POST)
        a = req.POST['firma']
        b = req.POST['juice']
        if a and not b:
            baza = Product.objects.filter(firma_id=a)
        elif b and not a:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(name=c)
        elif a and b:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(firma_id=a, name=c)
    for i in baza:
        bd.append((i.name, i.price, i.firma.title))
    title = ('Название', 'Цена', 'Фирма')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)


def table2(req):
    baza = Student.objects.all()
    anketa = FormStudents()
    bd = []
    if req.POST:
        anketa = FormStudents(req.POST)
        a = req.POST['course']
        b = req.POST['student']
        # if a and not b:
        #     baza = Student.objects.filter(firma_id=a)
        # elif b and not a:
        #     c = Product.objects.get(id=b).name
        #     baza = Product.objects.filter(name=c)
        # elif a and b:
        #     c = Product.objects.get(id=b).name
        #     baza = Product.objects.filter(firma_id=a, name=c)
    for i in baza:
        kursi = ', '.join(i.course.values_list('title', flat=True))
        bd.append((i.name, i.group, kursi))
    title = ('Имя', 'Группа', 'Курсы')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)
