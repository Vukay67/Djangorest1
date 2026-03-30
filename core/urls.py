from django.urls import path
from .views import HelloAPIView, ProductListAPIView, ProductRetrieveAPIView, test_view

urlpatterns = [
    path('test/', test_view),
    path('hello/', HelloAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
]
