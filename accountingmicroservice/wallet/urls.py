from django.urls import path
from .api import WalletList, WalletDetail, runnerTask

urlpatterns = [
    path('w/', WalletList.as_view()),
    path('w/<pk>/', WalletDetail.as_view()),

]
