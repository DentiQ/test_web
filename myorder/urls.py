from django.urls import path

from . import views

app_name = 'myorder'

urlpatterns = [
    path('', views.index, name='index'),
    path('orders', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/complete/<int:order_id>/', views.order_complete, name="order_complete"),
    path('order/my_order_list/', views.my_order_list, name="my_order_list"),

]