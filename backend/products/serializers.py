from rest_framework import serializers

from django import forms

from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
        
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance,validated_data)
    
    def get_my_discount(self,obj):
        return obj.get_discount()
        