"""xmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

# router = DefaultRouter()
# router.register(r'users',UserViewSet)
from account.views import UserViewSet
from address.views import AddressListView
from cart.views import CartViewSet
from order.views import OrderListViewSet
from xmall import settings
router = DefaultRouter()
router.register(r'user',UserViewSet,basename='user')
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'order',OrderListViewSet,basename='order')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    # path('api/',include(('account.urls','account'),namespace = 'account')),
    path('api/goods/',include(('goods.urls','goods'),namespace= 'goods')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/home/',include(('home.urls','home'),namespace = "home")),
    #生成jwt
    path('api/jwt-token-auth/',obtain_jwt_token),
    path('api/address/',include(('address.urls','address'),namespace="address")),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
