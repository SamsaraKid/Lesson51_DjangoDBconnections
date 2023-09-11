from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.title


class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)
