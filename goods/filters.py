from django_filters import rest_framework as filters

from goods.models import Good


class GoodsFilter(filters.FilterSet):
    """商品的过滤类"""
    # 区间查询,指定区间的最大最小值
    priceGt = filters.NumberFilter(field_name="salePrice", lookup_expr='gte')
    priceLte = filters.NumberFilter(field_name="salePrice", lookup_expr='lte')
    class Meta:
        model = Good
        fields = ['priceGt', 'priceLte']