from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.products.models import Category, Product
from apps.products.serializers import CategorySerializer, ProductsListSerializer


# Create your views here.


class CategoryListAPIViews(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class ProductListAPIViews(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'colours','sizes',)

    def get_queryset(self):
        queryset = super(ProductListAPIViews, self).get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if max_price and  min_price:
            queryset1 = queryset.filter(price__gte=min_price)
            queryset2 = queryset.filter(price__lte=max_price)
            return queryset1 | queryset2





