from django.urls import path
from .views import HelloAPIView, ProductAPIView, test_view

urlpatterns = [
    path('test/', test_view),
    path('hello/', HelloAPIView.as_view()),
    path('products/', ProductAPIView.as_view())
]
