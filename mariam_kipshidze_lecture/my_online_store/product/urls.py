from django.urls import path

from product.views import product_list, product_detail, product_create, product_update, product_delete

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('product_create/', product_create, name='product_create'),
    path('product_update/<int:pk>', product_update, name='product_update'),
    path('product_delete/<int:pk>', product_delete, name='product_delete'),
]
