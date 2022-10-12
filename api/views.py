
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Transaction, Wallet
from serializer import Accountserializer, Cardserializer, Customerserializer, Loanserializer, Notificationserializer, Receiptserializer, Transactionserializer, Walletserializer

# Create your views here.
class Customerviewsets(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class= Customerserializer

class Walletviewsets(viewsets.ModelViewSet):
    queryset= Wallet.objects.all()
    serializer_class= Walletserializer

class Accountviewsets(viewsets.ModelViewSet):
    queryset= Account.objects.all()
    serializer_class= Accountserializer

class Cardviewsets(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class= Cardserializer 

class Transactionviewsets(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class= Transactionserializer  

class Receiptviewsets(viewsets.ModelViewSet):
    queryset= Receipt.objects.all()
    serializer_class= Receiptserializer

class Notificationviewsets(viewsets.ModelViewSet):
    queryset= Notification.objects.all()
    serializer_class= Notificationserializer  
  

