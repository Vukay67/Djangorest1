from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

def test_view(request):
    return render(request, "test.html")

class HelloAPIView(APIView):
    def get(self, request):
        obj = {
            'message': 'Привет из апишки аманбол',
            'status': 'ЖАРАЙТ'
        }
        
        return Response(obj)
    
# class ProductAPIView(GenericAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     def get(self, request):
#         products = Product.objects.all()
#         serislizer = ProductSerializer(products, many=True)

#         return Response(serislizer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)

class ProductListAPIView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter

    ordering_fields = ['name', 'price']
    ordering = ['-name']

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class ProductRetrieveAPIView(GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

        if product:
            product.views_count += 1
            product.save()

        return self.retrieve(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def patch(self, request, pk):
        return self.update(request, pk)