from django.contrib import admin

# Register your models here.
from home.models import Navlist, Panel, Panelcontent


class NavlistAdmin(admin.ModelAdmin):
    list_display = ['name','panelId','type','sortOrder','fullUrl','id']
    list_filter = ['name']

class PanelcontentAdmin(admin.ModelAdmin):
    list_display = ['good_id','sort_order','panel_id','created','updated']
    search_fields = ['panel_id__name']
    list_filter = ['panel_id']
    list_per_page = 10

admin.site.register(Navlist,NavlistAdmin)
admin.site.register(Panel)
admin.site.register(Panelcontent,PanelcontentAdmin)
