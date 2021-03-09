from django.db import models

# Create your models here.


class Temp_Orders(models.Model):
    item = models.CharField(max_length=100)
    qty = models.CharField(max_length=2)
    table_no = models.CharField(max_length=20, default='')

    def __str__(self):
        return (self.item)




class Menu(models.Model):
    itemName = models.CharField(max_length = 100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return (self.itemName)


class Table(models.Model):
    tableName = models.CharField(max_length = 100)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return (self.tableName)

class Order(models.Model):
    table = models.OneToOneField(Table, on_delete=models.SET_NULL, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(str(self.table))

class OrderedItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, null = True)

    ordId = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default= 1)

    def __str__(self):
        return (str(self.item))

class Waiters(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=256)

    def __str__(self):
        return (self.name)

