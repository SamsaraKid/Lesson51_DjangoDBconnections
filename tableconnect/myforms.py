from django import forms
from .models import *


class FormJuice(forms.Form):
    all = Company.objects.all()
    mas = []
    for a in all:
        mas.append((a.id, a.title))
    # firma = forms.ChoiceField(choices=tuple(mas), required=False)
    # firma = forms.ModelChoiceField(all)
    firma = forms.ModelChoiceField(Company.objects.all(), required=False)
    juice = forms.ModelChoiceField(Product.objects.all(), required=False)
    # firma = forms.ModelChoiceField(Company.objects.values_list('title', flat=True), required=False)
    # juice = forms.ModelChoiceField(Product.objects.values_list('name', flat=True).distinct(), required=False)


class FormStudents(forms.Form):
    course = forms.ModelChoiceField(Course.objects.all(), required=False)
    student = forms.ModelChoiceField(Student.objects.all(), required=False)
