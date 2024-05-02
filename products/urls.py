from django.urls import path
from .views import get_info, get_item, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('products/<int:pk>', get_item, name='get_item'),
    path('products/detail/<int:pk>', detail, name='detail')
]
