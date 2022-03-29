from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    img_url=models.CharField(max_length=2083)


class Discount(models.Model):
    code=models.IntegerField(max_length=20)
    discountt=models.FloatField()
    discription=models.CharField(max_length=255)

