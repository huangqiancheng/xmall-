from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = "订单信息"

    #注册信号
    def ready(self):
        import order.signals