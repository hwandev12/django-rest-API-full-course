from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# Biz bu yerda api yaratishimiz hamda hamma apilarni ko'rishimiz ham mumkin bo'ladi
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()


# Bu yo'l ham bolaveradi hamma API larni korish uchun
class ProductListAPIView(generics.ListAPIView):
    """
    Not very Useful in here
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIView.as_view()