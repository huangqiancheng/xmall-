from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from cart.models import Cart
from goods.models import Good

from order import serializers
from order.models import Order, OrderGoods
from order.serializers import OrderSerializer, OrderListSerializer,OrderGoodsSerializer
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'

class OrderListViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination
    lookup_field = 'order_sn'
    def get_serializer_class(self):
        if self.action == "create":
            return OrderSerializer
        return OrderListSerializer
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.id)

    #返回订单实例
    def perform_create(self, serializer):
        return serializer.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        shop_carts = self.request.data['goods']
        for shop_cart in shop_carts:
            good = Good.objects.filter(id=shop_cart['good']['id']).first()
            order_goods = OrderGoods()
            order_goods.good = good
            order_goods.goods_num = shop_cart['good_num']
            order_goods.price = shop_cart['good']['salePrice']
            # print(order_goods.good)
            # print(order_goods.goods_num)
            order_goods.order =order
            order_goods.save()
            Cart.objects.filter(user_id=self.request.user.id,checked=True).all().delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
