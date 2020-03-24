from rest_framework import serializers

from goods.models import Category
from goods.serializers import GoodsListSerializers
from home.models import Navlist, Panel, Panelcontent


#导航栏类别
class NavlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navlist
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

#首页面板内容序列器
class PanelcontentListSerializer(serializers.ModelSerializer):
    # goods = GoodsListSerializers(many=True)
    class Meta:
        model = Panelcontent
        fields = "__all__"

#首页面板序列器，包含内容
class PanelSerializer(serializers.ModelSerializer):
    panels = PanelcontentListSerializer(many=True)
    class Meta:
        model = Panel
        fields = ("id","name","type","sort_order","position","limit_num","status","created","updated","panels")