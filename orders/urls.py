from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('table', views.table, name='table'),
    path('order', views.acceptOrder, name='order'),
    # path('temp', views.temp, name='temp'),
    # path('delete', views.delete, name='delete'),
    # path('confirm', views.confirm, name='confirm'),
    # path('kitchen', views.kitchen, name='kitchen'),
    path('menu', views.MenuList, name='menuList'),
    path('addmenu', views.addMenu, name = 'menu-add'),
    path('vieworder', views.viewOrder, name = 'vieworder'),
    path('tables', views.returnTable, name = 'tables'),
    path('createorder', views.createOrder, name = 'createorder'),
    path('login', views.login, name = 'login'),
    path('viewOrderedItem', views.viewOrderedItem, name='lists'),
    path('editOrder', views.editOrder, name='editOrder'),


]
