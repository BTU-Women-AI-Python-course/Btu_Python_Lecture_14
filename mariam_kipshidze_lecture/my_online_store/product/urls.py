from django.urls import path

from product.views import personal_info, check_age

urlpatterns = [
    path('personal_info/', personal_info, name='personal_info'),
    path('check_age/', check_age, name='check_age'),
]
