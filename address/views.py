from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from address.models import Address
from address.serializers import AddressListViewSerializers
from rest_framework import mixins, generics


class AddressListView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListViewSerializers
    #地址展示
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # 新增地址
    def post(self,request, *args, **kwargs):
        request.data['user_id'] = self.request.user.id
        if request.data['is_default'] == True:
            for i in Address.objects.all():
                i.is_default = False
                i.save()
        return self.create(request, *args, **kwargs)

class AddressListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListViewSerializers
    #修改默认地址
    def patch(self, request, *args, **kwargs):
        for i in Address.objects.all():
            i.is_default = False
            i.save()
        return self.partial_update(request, *args, **kwargs)