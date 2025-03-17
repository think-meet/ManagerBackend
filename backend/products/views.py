from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from core.models import Product
from .serializers import ProductSerializer

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(content=content)
    
    
product_list_create_view = ProductListCreateApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_fields = 'pk'
    
product_detail_view = ProductDetailApiView.as_view()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        
    
product_update_view = ProductUpdateApiView.as_view()

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_Destroy(instance)
    
product_delete_view = ProductDeleteApiView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)

        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True)
        return Response(data)
    
    if method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(riase_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            
            if content is None:
                content = title
            
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)
        