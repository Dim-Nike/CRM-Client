from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['create_id', 'status', 'pre_order']
    search_fields = ['verification']


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['serial_number']


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['client_phone']

admin.site.register(Device, DeviceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Specialist)
admin.site.register(OrderStatus)