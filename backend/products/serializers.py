from rest_framework import serializers
from . import validators

from django import forms

from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    name = serializers.CharField(source='title',read_only=True)
    class Meta:
        model = Product
        fields = [
            'user',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
        
    def get_my_user_data(self,obj):
        return {
            "username": obj.user.username
        }
     
    # def validate_title(self,value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user,title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value    
        
        
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
        