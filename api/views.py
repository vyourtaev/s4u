# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.http import , JsonResponse

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.models import Account, Transaction
from api.serializers import AccountSerializer, TransactionSerializer


def index(request):
    return HttpResponse("Test s4u")


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        # return Response('{"Status":"200","data":"data}')
        # return Response('{"Status":"200","data":{}}'.format(serializer.data))
        return Response(serializer.data)

    def retriev(self, request, pk=None):
        queryset = self.get_queryset()
        account = get_object_or_404(queryset, pk=pk)
        serializer = AccountSerializer(account)
        # return Response('{"Status":"500}')

        return Response({"Error": status.HTTP_201_CREATED, "data": serializer.data})


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        return Response('{"Status":"200","data":"{}}'.format(serializer.data))
        # return Response(serializer.data)


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
