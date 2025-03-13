from rest_framework import generics

from core.models import Product
from .serializers import ProductSerializer

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        serializer.save()
    
    
product_create_view = ProductCreateApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_fields = 'pk'
    
product_detail_view = ProductDetailApiView.as_view()