from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from django.http import JsonResponse


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
