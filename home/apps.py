from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    # 修改在Django后台中应用的显示名称
    verbose_name = "导航栏及首页信息"