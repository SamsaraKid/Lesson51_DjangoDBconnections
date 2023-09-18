from django.shortcuts import render, redirect
from .models import *
from .myforms import *
from random import choice


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

    # volumes = (0.25, 0.33, 1.0, 1.5, 2.0)
    # packs = ('plactic', 'glass', 'tetrapak')
    # recom = (True, False)
    # for juice in Product.objects.all():
    #     juice.volume = choice(volumes)
    #     juice.pack = choice(packs)
    #     juice.recomend = choice(recom)
    #     juice.save()

    # s1 = Student.objects.create(name='Viktor', group='G001')
    # s2 = Student.objects.create(name='Igor', group='G001')
    # s3 = Student.objects.create(name='Alex', group='G001')
    # s4 = Student.objects.create(name='Zahar', group='G002')
    # s5 = Student.objects.create(name='Andrey', group='G002')
    # k1 = Course.objects.create(title='Math')
    # k2 = Course.objects.create(title='Geo')
    # k1.student_set.add(s1, s3, s5)
    # k2.student_set.add(s1, s2, s3)

    # u1 = User.objects.create(name='Alex')
    # ac1 = Account.objects.create(login='qwe', password='12345', user=u1)
    # u2 = User.objects.create(name='Igor')
    # ac1 = Account.objects.create(login='asd', password='67890', user=u2)

    return redirect('index')


def table1(req):
    baza = Product.objects.all()
    anketa = FormJuice()
    bd = []
    if req.POST:
        anketa = FormJuice(req.POST)
        if anketa.is_valid():
            data = anketa.cleaned_data
            if data['firma']:
                data['firma'] = Company.objects.get(title=data['firma']).id
            search = {k: v for (k, v) in data.items() if v != None}
            baza = Product.objects.filter(**search)

        # if a and not b:
        #     baza = Product.objects.filter(firma_id=a)
        # elif b and not a:
        #     c = Product.objects.get(id=b).name
        #     baza = Product.objects.filter(name=c)
        # elif a and b:
        #     c = Product.objects.get(id=b).name
        #     baza = Product.objects.filter(firma_id=a, name=c)
    for i in baza:
        bd.append((i.name, i.price, i.firma.title, i.volume, i.pack, i.recomend))
    title = ('Название', 'Цена', 'Фирма', 'Объём', 'Упаковка', 'Рекомендован')
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
        search = {}
        if a:
            search.update({'course': a})
        if b:
            search.update({'id': b})
        baza = Student.objects.filter(**search)

    for i in baza:
        kursi = ', '.join(i.course.values_list('title', flat=True))
        bd.append((i.name, i.group, kursi))
    title = ('Имя', 'Группа', 'Курсы')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)


def table3(req):
    baza = User.objects.all()
    anketa = ''
    bd = []
    # if req.POST:
    #     anketa = FormStudents(req.POST)
    #     a = req.POST['course']
    #     b = req.POST['student']
    #     search = {}
    #     if a:
    #         search.update({'course': a})
    #     if b:
    #         search.update({'id': b})
    #     baza = Student.objects.filter(**search)

    for i in baza:
        bd.append((i.name, i.account.login, i.account.password))
    title = ('Имя', 'Логин', 'Пароль')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)
