from rest_framework import generics
from rest_framework.filters import SearchFilter

from electronic.models import Seller
from electronic.permissions import IsActiveUser
from electronic.serializers import SellerSerializer, SellerDetailSerializer, SellerUpdateSerializer


class SellerListCreateAPIView(generics.ListCreateAPIView):
    """Представление для создания продавца и отображения списка"""
    serializer_class = SellerSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['title']
    queryset = Seller.objects.all()
    permission_classes = [IsActiveUser]


class SellerUpdateAPIView(generics.UpdateAPIView):
    """Представление для обновления продавца"""
    serializer_class = SellerUpdateSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsActiveUser]


class SellerDetailAPIView(generics.RetrieveDestroyAPIView):
    """
    Представление для просмотра и удаления отдельного продавца
    """
    serializer_class = SellerDetailSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsActiveUser]

