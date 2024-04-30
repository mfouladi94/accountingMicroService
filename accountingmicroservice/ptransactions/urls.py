from django.urls import path
from .api import TransactionList, TransactionDetail

urlpatterns = [
    path('transactions/', TransactionList.as_view()),
    path('transactions/<pk>/', TransactionDetail.as_view()),
]
