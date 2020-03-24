from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from goods.models import Category
from home.models import Navlist, Panel
from home.serializers import NavlistSerializer, CategoryListSerializer, PanelSerializer


#导航栏展示视图（导航栏id商品id，方便查询）
class NavlistView(generics.ListAPIView):
    queryset = Navlist.objects.all()
    serializer_class = NavlistSerializer
    authentication_classes = []

#首页导航栏商品分类视图
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    authentication_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(parent_id=None)

#首页视图
class PanelListView(generics.ListAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
    authentication_classes = []