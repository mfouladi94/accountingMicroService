from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet
from .serializers import WalletSerializer
from .tasks import *
from ..utils.micro_auth import valid_authorization


class WalletList(APIView):
    def get(self, request):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)

    def post(self, request):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetail(APIView):
    def get_object(self, pk):
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

    def put(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        if not valid_authorization(request):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        wallet = self.get_object(pk)
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def runnerTask(request):
    my_task.delay()
    return HttpResponse('Task done')
