from django.db import models

# Create your models here.
from account.models import User
from goods.models import Good


class CartManager(models.Manager):
    def update_or_create(self, good_num=1, **kwargs):
        cart, created = self.get_or_create(**kwargs)
        if created:
            cart.good_num = good_num
        else:
            cart.good_num += good_num
        cart.save()
        return cart, created

class Cart(models.Model):
    good = models.ForeignKey(Good,verbose_name="商品名",related_name="cart_good_id",on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,verbose_name="用户名",related_name="cart_user_id",on_delete=models.CASCADE,null=True,blank=True)
    good_num = models.PositiveIntegerField(verbose_name="商品数量",default=0)
    checked = models.BooleanField(default=False,verbose_name="是否被选中")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    objects = CartManager()

    def __str__(self):
        return self.good.productName
    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ['good', 'user']


