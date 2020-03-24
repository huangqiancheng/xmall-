from random import choice

from django.db import models

# Create your models here.
from django.utils.timezone import now

from account.models import User

# 随机获取订单号
from goods.models import Good
from xmall import settings


def get_order_id():
    order_id = now().strftime("%Y%m%d%H%M%S%f")
    status_id = []
    status = "0123456789"
    for i in range(6):
        status_id.append(choice(status))
    return order_id + "".join(status_id)

def get_order_timeout():
    return now()+ settings.order_timeout

class Order(models.Model):
    # 未支付
    STATUS_PAY = 1
    # 未发货
    STATUS_NODELIVER = 2
    # 已发货,待收货
    STATUS_YETDELIVER = 3
    # 确认收货
    STATUS_RECEIVE = 4
    # 已过期
    STATUS_TIMEOUT = 5
    # 已取消
    STATUS_CANCEL = 6

    STATUS_CHOICES = (
        (STATUS_PAY, '未支付'),
        (STATUS_NODELIVER, '未发货'),
        (STATUS_YETDELIVER, '已发货'),
        (STATUS_RECEIVE, '确认收货'),
        (STATUS_TIMEOUT, '已过期'),
        (STATUS_CANCEL, '已取消'),

    )

    order_sn = models.CharField(max_length=30,verbose_name="订单号",blank=True,null=True,unique=True,editable=False)
    trade_no = models.CharField(max_length=100,verbose_name="产品编号",unique=True,null=True,blank=True)
    pay_status =  models.CharField(verbose_name='订单状态', max_length=30, choices=STATUS_CHOICES, default=STATUS_PAY)
    post_script = models.CharField(max_length=200,verbose_name="附言",null=True,blank=True)
    order_total =  models.DecimalField(max_digits=10,decimal_places=2,verbose_name ='订单金额',default=0.00)
    pay_time = models.DateTimeField(null=True,blank=True,verbose_name="付款时间")
    address = models.CharField("收货信息",max_length=100)
    singer_name = models.CharField(max_length=20,verbose_name="姓名")
    singer_mobile = models.CharField(max_length=11,verbose_name="联系电话")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    user = models.ForeignKey(User,related_name="order_user_id",on_delete=models.CASCADE,verbose_name="用户名")
    close_time = models.DateTimeField(verbose_name="订单完成时间",default=get_order_timeout)

    def __str__(self):
        return self.user.username + "----" + str(self.order_sn)

    class Meta:
        ordering = ['-created']
        verbose_name = "订单"
        verbose_name_plural = verbose_name

class OrderGoods(models.Model):
    goods_num = models.PositiveIntegerField(verbose_name="商品数量")
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name ='价格')
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    order = models.ForeignKey(Order,related_name="order",on_delete=models.CASCADE,verbose_name="订单")
    good = models.ForeignKey(Good,related_name="good",on_delete=models.CASCADE,verbose_name="商品名")

    def __str__(self):
        return self.good.productName

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name


