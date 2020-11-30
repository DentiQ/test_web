from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dish(models.Model):
    dishname = models.TextField()
    dishtype = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.dishname


class Tableware(models.Model):
    tablewarename = models.TextField()
    tablewaretype = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.tablewarename


class Style(models.Model):
    stylename = models.TextField()
    tablewares = models.ManyToManyField('Tableware')
    price = models.IntegerField()

    def getprice(self):
        return self.price

    def __str__(self):
        return self.stylename


class Dinner(models.Model):
    dinnername = models.TextField()
    dishes = models.ManyToManyField('Dish')
    appliablestyle = models.ManyToManyField('Style')
    price = models.IntegerField()

    def aplliablestyle(self):
        return self.appliablestyle

    def getprice(self):
        return self.price

    def __str__(self):
        return self.dinnername


class Order(models.Model):
    username = models.TextField()

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    dinner = models.ForeignKey('Dinner', on_delete=models.CASCADE, default=None)

    style = models.ForeignKey('Style', on_delete=models.CASCADE, default=None)

    details = models.TextField()
    people = models.IntegerField(default=1)
    address = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return str(self.username) + '\'s order at ' + str(self.create_date)
