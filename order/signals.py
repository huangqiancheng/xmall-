from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import Order
from xmall.redis import redis
# from datetime import timedelta


@receiver(post_save, sender=Order)
def save_order_status(sender, instance, created, **kwargs):
    if created:
        redis.zadd('time',instance.created.timestamp(),instance.order_sn)