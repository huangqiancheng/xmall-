from django.urls import path

from home import views

urlpatterns = [
    path('navList/',views.NavlistView.as_view(),name ="home-navlist"),
    path("category/" , views.CategoryListView.as_view(), name = "home-category"),
    path("",views.PanelListView.as_view(),name="home")
]