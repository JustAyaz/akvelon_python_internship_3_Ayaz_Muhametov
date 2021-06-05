from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from finances.serializers import *
from finances.models import *
from finances.service import *


def blanc(request):
    return HttpResponse('Hello there!')


# use this to create new user
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


# use this to retrieve/update/destroy information about user
class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


# use this to create new transaction
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionDetailSerializer


# use this to retrieve/update/destroy information about transaction
class TransactionRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionDetailSerializer
    queryset = Transaction.objects.all()


# use this to get all user's transactions
class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = TransactionListSerializer(user)
        return Response(serializer.data)


# here i'm trying to make daily total, but smth goes wrong
class UserDailyTotalView(APIView):
    def get(self, request, pk):
        total = User.objects.filter(id=pk)\
            .values('transactions__date')\
            .order_by('transactions__date')\
            .annotate(sum=Sum('transactions__amount'))

        serializer = TransactionTotalSerializer(total, many=True)
        return Response(serializer.data)


# i couldn't make the right one, but I have this one. Outputs the total amount
class UserTotalView(APIView):
    def get(self, request, pk):
        total = User.objects.filter(id=pk).annotate(
            total_amount=models.Sum(models.F('transactions__amount')))

        serializer = TransactionTotalSerializer(total, many=True)
        return Response(serializer.data)