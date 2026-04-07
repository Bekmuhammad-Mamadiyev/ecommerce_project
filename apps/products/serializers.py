from rest_framework import serializers

from apps.common.serializers import MediaSerializer
from apps.products.models import *
from apps.products.utils import validate_rating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'image', 'description', 'discount','brand','thumbnail', 'in_stock']

class ProductColorListSerializer(serializers.Serializer):
    colour = MediaSerializer(read_only=True)
    id = serializers.IntegerField()


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSizeSerializer(serializers.Serializer):
    value = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField()

class ProductReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('title','rank','email', 'created_at', )

class AddReviewSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = ProductReview


    def validate_rank(self, rank):
        if validate_rating(rank):
            return rank
        else:
            raise serializers.ValidationError({'rank': 'This field is required'})