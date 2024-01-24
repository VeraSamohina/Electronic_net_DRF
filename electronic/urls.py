from django.urls import path

from electronic.apps import ElectronicConfig
from electronic.views import SellerListCreateAPIView, SellerDetailAPIView, SellerUpdateAPIView

app_name = ElectronicConfig.name

urlpatterns = [
    path('create/', SellerListCreateAPIView.as_view(), name='seller-create'),
    path('', SellerListCreateAPIView.as_view(), name='seller-list'),
    path('<int:pk>/', SellerDetailAPIView.as_view(), name='seller-retrieve'),
    path('<int:pk>/update/', SellerUpdateAPIView.as_view(), name='seller-update'),
    path('<int:pk>/delete/', SellerDetailAPIView.as_view(), name='seller-delete'),
    ]
