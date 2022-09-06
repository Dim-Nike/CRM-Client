from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['create_id', 'status', 'pre_order']
    search_fields = ['verification']
    list_display = ['master', 'order_client', 'status', 'verification', 'pre_order', 'create_id']


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['serial_number']
    list_display = ['model', 'manufacturer', 'serial_number', 'count']


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['client_name']
    list_display = ['client_name', 'client_phone', 'client_mail', 'form_of_appeal', 'client_time']
    list_filter = ['form_of_appeal', 'client_time']

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'phone', 'count_day_work']


admin.site.register(Device, DeviceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(OrderStatus)