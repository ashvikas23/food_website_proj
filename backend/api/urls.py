from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.get_restaurants),
    path('menu/<int:rid>/', views.get_menu),
    path('place-order/', views.place_order),
    path('orders/', views.get_orders),
    path('order-items/<int:oid>/', views.get_order_items),


]
