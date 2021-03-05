from rest_framework import serializers
from .models import Menu, Order, Table, OrderedItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
  table = TableSerializer(read_only = True)

  class Meta:
    model = Order
    fields = ('id', 'table', 'dateCreated')

class OrderedItemSerializer(serializers.ModelSerializer):
    
    item = ItemSerializer(read_only=False)

    class Meta:
        model = OrderedItem
        fields = ( 'item', 'quantity')

# class OrderedItemSerializer(serializers.ModelSerializer):
    
#     items = OrderSerializer()
#     class Meta:
#         model = OrderedItem
#         fields = ('id', 'quantity', 'items')


# {'name': 'roti', 'ingredients': {'protein': 10.0, 'carb': 10.0, 'fat': 10.0}     
# {'name': 'rice', 'ingredients': [OrderedDict([('id', 1), ('protein', 56.0), ('carb', 89.0), ('fat', 89.0), ('product', 1)])]}  

# from orders.models import OrderedItem
# items = OrderedItem.objects.all()
# item = items[1]
# print(item)
# from orders.serializers import OrderedItemSerializer
# serializer = OrderedItemSerializer(item)
# print(serializer.data)
