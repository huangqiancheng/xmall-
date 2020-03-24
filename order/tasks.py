

from django.utils.timezone import now

from order.models import Order
from xmall.redis import redis
from xmall.settings import order_timeout

time = (now() - order_timeout).timestamp()
def check_order_status():
    order = redis.zrangebyscore('time',min=0,max=time)
    order_sn = [str(i).split("'")[1] for i in order]
    order_list = Order.objects.filter(order_sn__in=order_sn)
    for j in order_list:
        j.pay_status=Order.STATUS_TIMEOUT
        j.save()
    return order_list
