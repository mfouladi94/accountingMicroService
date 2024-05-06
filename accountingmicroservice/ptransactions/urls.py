from django.urls import path
from .api import TransactionList, TransactionDetail , TransactionCreate , public_view

urlpatterns = [
    path('t/', TransactionList.as_view()),
    path('t/<pk>/', TransactionDetail.as_view()),
    path('t/create/', public_view),


]
