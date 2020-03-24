from django.db import models

# Create your models here.
from account.models import User


class Address(models.Model):
    name = models.CharField(max_length=20,verbose_name ="收件人",null=True,blank=True)
    tel = models.CharField(max_length=11,verbose_name="电话号码",null=True,blank=True)
    address = models.CharField(max_length=150,verbose_name="收货地址",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="address_user_id",verbose_name ="用户名")
    is_default = models.BooleanField(default=False, verbose_name ="是否为默认收货地址")

    class Meta:
        verbose_name ="收货地址"
        verbose_name_plural = verbose_name
        ordering = ('-is_default',)

    def __str__(self):
        return self.name+"***"+self.address

