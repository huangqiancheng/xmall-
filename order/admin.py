from django.contrib import admin

# Register your models here.
from order.models import Order,OrderGoods

class OrderGoodsAdmin(admin.TabularInline):
    model = OrderGoods

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_sn','pay_status','order_total','pay_time','address','user']
    list_filter = ['user']
    search_fields = ['singer_name','user__username']
    list_per_page = 10
    inlines = [OrderGoodsAdmin]
admin.site.register(Order,OrderAdmin)
