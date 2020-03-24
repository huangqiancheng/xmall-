from django.urls import path

from address import views

urlpatterns = [
    path('',views.AddressListView.as_view(),name = "addresslist"),
    path('<pk>/',views.AddressListDetailView.as_view(),name="addresslist-detail"),
]