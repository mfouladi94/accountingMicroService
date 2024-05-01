from django.urls import path
from .api import TransactionList, TransactionDetail

urlpatterns = [
    path('', TransactionList.as_view()),
    path('<pk>/', TransactionDetail.as_view()),
]
