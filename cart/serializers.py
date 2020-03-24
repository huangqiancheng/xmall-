from rest_framework import serializers

from cart.models import Cart
from goods.models import Good
from goods.serializers import GoodsListSerializers


class CreateCarterializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    good_num = serializers.IntegerField(required=True,label="数量",min_value =1,)
    good = serializers.PrimaryKeyRelatedField(required=True,queryset=Good.objects.all())
    checked = serializers.BooleanField(default=True)
    def create(self, validated_data):
        instance,created = Cart.objects.update_or_create(**validated_data)
        return instance
    def update(self,instance,validated_data):
        instance.good_num = validated_data['good_num']
        instance.checked = validated_data["checked"]
        instance.save()
        return instance
class CartListSerializers(serializers.ModelSerializer):
    good = GoodsListSerializers()
    class Meta:
        model = Cart
        fields = "__all__"



