from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CreateCarterializers, CartListSerializers


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    # serializer_class = CreateCarterializers
    pagination_class = None

    # 使用DRF视图集时自定义action方法,url即为当前函数名
    #购物车全选功能
    @action(methods=['post'], detail=False)
    def EditCheckAll(self, request):
        user = request.user.id
        cart_list = Cart.objects.filter(user=user)
        checked = request.data['checked']
        for cart in cart_list:
            cart.checked = checked
            cart.save()
        return Response({'success': True})

    #购物车删除选中商品功能
    @action(methods=['post'], detail=False)
    def DelCartChecked(self, request):
        user = request.user.id
        # print(Cart.objects.filter(user=user, checked=True))
        Cart.objects.filter(user=user, checked=True).all().delete()
        return Response({'success': True})


    def get_queryset(self):
            return self.queryset.filter(user=self.request.user.id)
    def get_serializer_class(self):
        if self.action == "list":
            serializer_class = CartListSerializers
            return serializer_class
        elif self.action == "partial_update":
            serializer_class = CreateCarterializers
            return serializer_class
        else:
            serializer_class = CreateCarterializers
            return serializer_class

