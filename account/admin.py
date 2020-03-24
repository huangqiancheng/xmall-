from django.contrib import admin

# Register your models here.
from account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','mobile','last_login','date_joined','is_superuser']
    search_fields = ['username']
    list_filter = ['last_login', 'date_joined','is_superuser']
admin.site.register(User,UserAdmin)