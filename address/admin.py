from django.contrib import admin

# Register your models here.
from address.models import Address
class AddressAdmin(admin.ModelAdmin):
    list_display = ['name','tel','address','user_id','is_default','created','updated']
    search_fields = ['name','address','tel','user_id__username']
    list_filter = ['name','user_id']
    list_per_page = 10
    date_hierarchy = 'updated'
    # list_editable = ['name']
    list_editable = ['tel','address','user_id','is_default']

admin.site.register(Address,AddressAdmin)