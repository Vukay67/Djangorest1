from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

def test_view(request):
    return render(request, "test.html")

class HelloAPIView(APIView):
    def get(self, request):
        obj = {
            'message': 'Привет из апишки аманбол',
            'status': 'ЖАРАЙТ'
        }
        
        return Response(obj)
    
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serislizer = ProductSerializer(products, many=True)

        return Response(serislizer.data)
