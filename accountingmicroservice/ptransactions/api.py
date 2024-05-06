from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from .serializers import TransactionSerializer
from ..utils.micro_auth import valid_authorization, get_user_id
from accountingmicroservice.wallet.models import *
from .tasks import *


class TransactionList(APIView):
    authentication_classes = []
    def get(self, request):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetail(APIView):
    authentication_classes = []
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionCreate(APIView):
    authentication_classes = []

    def get(self, request):
        return Response("hi")

    def post(self, request):
        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = get_user_id(request)

        wallet, _ = Wallet.objects.get_or_create(userId=user_id)
        amount = request.data.get('amount')
        transaction_type = request.data.get('type')
        transaction = Transaction.objects.create(wallet=wallet, amount=amount, type=transaction_type)
        update_wallet_balance.delay(transaction.id)
        return Response({'message': 'Transaction initiated'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([])
def public_view(request):
    return Response({'message': 'This is a public view'})
