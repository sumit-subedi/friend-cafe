import sys

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import status

from orders.serializers import ItemSerializer, OrderSerializer, TableSerializer, OrderedItemSerializer


from orders.models import Order, Temp_Orders, Menu, Table, OrderedItem, Waiters
# Create your views here.


def home(request):
    return render(request, 'home.html')


# def table(request):
#     tablename = request.GET['name']
#     t = Temp_Orders.objects.filter(table_no=tablename)
#     return render(request, 'table.html', {'table': tablename, 't': t})


# def orde(request):
#     val = Orders.objects.all()
#     return render(request, 'order.html', {'order': val})

def MenuList(request):
    
    items = Menu.objects.all()
    serializer = ItemSerializer(items, many = True)
    
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
def addMenu (request):
    
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def viewOrder(request):
    items = Order.objects.all()
    serializer = OrderSerializer(items, many = True)
    return JsonResponse(serializer.data, safe = False)

def viewOrderedItem(request):
    print(request.GET['id'])
    items = OrderedItem.objects.filter(ordId = request.GET['id'])
    serializer = OrderedItemSerializer(items, many = True)
    return JsonResponse(serializer.data, safe = False)



@api_view(['POST'])
def createOrder(request):
    try:
        table = Table.objects.get(pk = request.data['tid'])
        order = Order.objects.create(table = table)
    
        for item in request.data['OrderedItem']:
            if item['itemid'] == "":
                continue
            menu = Menu.objects.get(pk = item['itemid'])
            OrderedItem.objects.create(ordId = order, item = menu , quantity = item['quantity'])

        table.occupied = True
        table.save()
        return Response("OK", status=status.HTTP_201_CREATED)
    except :
        order.delete()
        return Response("Table not empty", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def editOrder(request):
    
    # table = Table.objects.get(pk = request.data['tid'])
    order = Order.objects.get(pk = request.data['ordId'])
    print(OrderedItem.objects.filter(ordId=request.data['ordId']).delete())

    for item in request.data['OrderedItem']:
        if item['itemid'] == "":
            continue
        menu = Menu.objects.get(pk = item['itemid'])
        OrderedItem.objects.create(ordId = order, item = menu , quantity = item['quantity'])

    return Response()
        




def returnTable (request):
    items = Table.objects.all().filter( occupied=False)
    serializer = TableSerializer(items, many = True)
    return JsonResponse(serializer.data, safe = False)

def temp(request):
    item = request.GET['item']
    qty = request.GET['qty']
    table = request.GET['table']
    t = Temp_Orders(item=item, qty=qty, table_no=table)
    t.save()
    url = '/table?name='+table
    return redirect(url)


def delete(request):
    item = request.GET['item']
    table = request.GET['table']
    d = Temp_Orders.objects.get(item=item, table_no=table)
    d.delete()
    url = '/table?name='+table
    return redirect(url)


def confirm(request):
    table = request.GET['table']
    t = Temp_Orders.objects.filter(table_no=table)
    for val in t:
        f = Orders(item=val.item, qty=val.qty, table_no=val.table_no)
        f.save()
    Temp_Orders.objects.all().delete()
    return redirect('/')


def kitchen(request):
    to = Orders.objects.all()
    return render(request, 'kitchen.html', {'t': to})

def acceptOrder(request):
    if request.method == "POST":
        pass
    else:

        return HttpResponseNotFound()

@api_view(['POST'])
def login(request):
    print(request.COOKIES)
    try:
        exists = Waiters.objects.get(name=request.data['name'])
    
        if exists:
            if exists.password == request.data['password']:
                response = Response() 
                response.set_cookie('username', request.data['name'], max_age=30*60)  
                return response
                
            else:
                raise Exception("Password dont match")
    except :
        
        return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
