import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from core.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# def api_home(request):
#     body = request.body
#     try:
#         data = json.loads(body)
#     except:
#         data = {}
    
#     print(data.keys)
#     print(request.GET)
#     print(request.POST)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse({"message":"Hi API Response"})

@api_view(['GET','POST'])
def api_home(request):
    
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        print(data)
        data = serializer.data
    return Response(data)