from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.title


class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=4, decimal_places=2)
    pack = models.CharField(max_length=10)
    recomend = models.BooleanField(null=True)

    # def __str__(self):
    #     return self.name


class Course(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=10)
    group = models.CharField(max_length=4)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
