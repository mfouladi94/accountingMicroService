from django.urls import path
from .api import WalletList, WalletDetail, runnerTask

urlpatterns = [
    path('', WalletList.as_view()),
    path('<pk>/', WalletDetail.as_view()),

]
