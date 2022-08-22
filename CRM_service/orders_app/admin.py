from django.contrib import admin
from .models import *




# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'manufacturer', 'model')
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'device', 'customer', 'order_description', 'create_id', 'last_updated_dt', 'order_status')
#
#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


# class DeviceInFieldAdmin(admin.ModelAdmin):
#     list_display = ('id', 'serial_number', 'analyzer_id', 'owner_status')


admin.site.register(Device)
admin.site.register(Customer)
admin.site.register(DeviceInField)
admin.site.register(Order)
admin.site.register(TestClass)
# admin.site.register(Client)
# admin.site.register(Specialist)
