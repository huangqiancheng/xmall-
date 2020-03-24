from django.urls import path

from goods import views

urlpatterns = [
    # path('',views.GoodsView.as_view(),name ='goods')
    path('',views.GoodsListView.as_view(),name='good'),
    path('<pk>/',views.GoodListDetailView.as_view(),name="good-detail"),

]
