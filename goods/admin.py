from django.contrib import admin

# Register your models here.
from goods.models import Goodimage, Good, Category

class GoodimageInline(admin.TabularInline):
    model = Goodimage

class GoodAdmin(admin.ModelAdmin):
    list_display = ['productName','salePrice','category_id','created','updated','id']
    #列表过滤器
    list_filter = ['productName','created']
    #后台商品展示上方日期层级导航栏
    date_hierarchy = 'created'
    #搜索项
    search_fields = ['productName']
    #指定可以在列表页进行编辑的字段
    list_editable = ['salePrice']
    list_per_page = 10
    inlines = [GoodimageInline,]




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','parent_id','created','updated','id']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Good,GoodAdmin)
