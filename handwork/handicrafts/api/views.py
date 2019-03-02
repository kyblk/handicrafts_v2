from rest_framework import viewsets

from .serializers import MainSliderSerializer, CatalogSerializer, ProductListSerializer
from ..models import MainSlider, Catalog, Product


class MainSliderViewSet(viewsets.ModelViewSet):
    queryset = MainSlider.objects.filter(is_visible=True)
    serializer_class = MainSliderSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.filter(is_visible=True)
    serializer_class = CatalogSerializer


class ProductListViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.filter(catalog__slug=self.kwargs.get('slug'), is_visible=True)
