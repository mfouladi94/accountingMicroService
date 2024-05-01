from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from .serializers import TransactionSerializer
from ..utils.micro_auth import valid_authorization


class TransactionList(APIView):
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
