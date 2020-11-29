from django.urls import path

from . import views

app_name = 'myorder'

urlpatterns = [
    path('', views.index),
    path('orders', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/create/', views.order_create, name='order_create'),

]