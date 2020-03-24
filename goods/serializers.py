from rest_framework import serializers


from goods.models import Good, Goodimage


#商品列表展示序列器


class GoodsListSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Good
        fields = ('id','salePrice', 'productName', 'subTitle','detail', 'productImageBig', 'created', 'updated')

class GoodimageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goodimage
        fields = "__all__"

class GoodDetailSerializers(serializers.ModelSerializer):
    image = GoodimageSerializers(many=True)
    class Meta:
        model = Good
        fields = "__all__"