from random import choice

from django.utils.timezone import now
from rest_framework import serializers

from goods.serializers import GoodsListSerializers
from order.models import Order, OrderGoods


#创建订单序列器
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pasy_status = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    #生成随机订单号
    def get_order_id(self):
        order_id = now().strftime("%Y%m%d%H%M%S%f")
        status_id = []
        status = "0123456789"
        for i in range(6):
            status_id.append(choice(status))
        return order_id + "-" + "".join(status_id) + "-" + str(self.context['request'].user.id)

    #生成订单实例
    def validate(self,attrs):
        attrs['order_sn'] = self.get_order_id()
        # print(attrs)
        return attrs
    class Meta:
        model = Order
        fields = "__all__"




class OrderGoodsSerializer(serializers.ModelSerializer):
    good = GoodsListSerializers()
    class Meta:
        model = OrderGoods
        fields = "__all__"

#列表展示序列器
class OrderListSerializer(serializers.ModelSerializer):
    #将订单商品包含在订单中一起进行序列化
    order = OrderGoodsSerializer(many=True)
    class Meta:
        model = Order
        fields = "__all__"