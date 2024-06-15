from django.urls import path
from .views import *

urlpatterns = [
    path('list/', BlogListAPIView.as_view(), name='api-list'),
    path('detail/<pk>', BlogDetailAPIView.as_view(), name='api-detail'),
    path('update/<pk>', BlogUpdateAPIView.as_view(), name='api-update'),
    path('delete/<pk>', BlogDeleteAPIView.as_view(), name='api-delete'),
]
