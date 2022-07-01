
from .models import ActiveIngredient, Product
from rest_framework import viewsets
from .serializers import ActiveIngredientSerializer, ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ActiveIngredientViewSet(viewsets.ModelViewSet):
    queryset = ActiveIngredient.objects.all()
    serializer_class = ActiveIngredientSerializer

# def get_serializer_class(self):
#     print(self.action)
#     """Retorna clase de serializador apropiadas
#         si es retrieve se usa el detalle"""
#     if self.action == 'retrieve':
#         return ProductDetailSerializer
#     return self.serializer_class
