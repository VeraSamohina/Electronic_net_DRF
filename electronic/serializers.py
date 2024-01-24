from rest_framework import serializers

from electronic.models import Seller
from electronic.validators import SellerLevelValidator


class SellerSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели продавца"""

    validators = [SellerLevelValidator(level='level', provider='provider')]


    class Meta:
        model = Seller
        fields = '__all__'


class SellerUpdateSerializer(serializers.ModelSerializer):
    """Сериалайзер для обновления продавца
    поле 'задолженность' только для чтения"""

    debt = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для детальной модели продавца"""
    provider = serializers.CharField(source="provider.title")
    product = serializers.CharField(source="product.title")
    product_model = serializers.CharField(source="product.product_model")
    launch_date = serializers.CharField(source="product.launch_date")

    class Meta:
        model = Seller
        fields = '__all__'
