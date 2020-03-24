from django.contrib import admin

# Register your models here.
from cart.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['good','user','good_num','checked']
    list_filter = ['user']
    list_editable = ['good_num','checked']
    list_per_page = 10


admin.site.register(Cart,CartAdmin)