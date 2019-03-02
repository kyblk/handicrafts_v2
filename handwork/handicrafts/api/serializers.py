from rest_framework import serializers

from ..models import MainSlider, Catalog, Product, ProductImage


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ('id', 'image', 'text')


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'label', 'image', 'slug', 'get_url')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductListSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('catalog', 'id', 'label', 'price', 'description', 'images', 'get_url')
