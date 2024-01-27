from rest_framework import serializers
from electronic.models import Seller, Product
from electronic.validators import SellerLevelValidator


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели Product(Продукт).
    """
    class Meta:
        model = Product
        fields = '__all__'


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

    provider = serializers.SlugRelatedField(slug_field='title', queryset=Seller.objects.all())
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Seller
        fields = '__all__'
