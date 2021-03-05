from django.contrib import admin

# Register your models here.
from .models import Temp_Orders,Order, Menu, Table, OrderedItem, Waiters

admin.site.register(Temp_Orders)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(OrderedItem)
admin.site.register(Waiters)



