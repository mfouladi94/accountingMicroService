from django.urls import path
from .api import WalletList, WalletDetail

urlpatterns = [
    path('wallets/', WalletList.as_view()),
    path('wallets/<pk>/', WalletDetail.as_view()),
]
