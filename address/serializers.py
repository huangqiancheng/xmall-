from rest_framework import serializers

from address.models import Address


class AddressListViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
