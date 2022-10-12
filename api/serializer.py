# from dataclasses import field
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Wallet


class Customerserializer(serializers.ModelSerializer):
   class Meta:
      model=Customer
      field = ("firstname","lastname","email")

class Walletserializer(serializers.ModelSerializer):
       class Meta:
         model=Wallet
         field = ("balance","currency","status")  

class Accountserializer(serializers.ModelSerializer):
       class Meta:
         model=Account
         field = ("account_number","account_type","password")

class Cardserializer(serializers.ModelSerializer):
       class Meta:
         model=Card
         field = ("card_number","user_name","date_issue") 

class Transactionserializer(serializers.ModelSerializer):
       class Meta:
         model=Card
         field = (" transaction_code","wallet"," transaction_amount") 

class Loanserializer(serializers.ModelSerializer):
       class Meta:
         model= Loan
         field = ("loan_number","loan_type","amount") 

class Receiptserializer(serializers.ModelSerializer):
       class Meta:
         model= Receipt
         field = ("receiptdate","Number","file")

class Notificationserializer(serializers.ModelSerializer):
       class Meta:
         model= Notification
         field = ("id","name"," date_and_time")                             