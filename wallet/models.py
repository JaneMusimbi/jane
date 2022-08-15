from django.db import models
from datetime import datetime
# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=15,null=True)
    lastname=models.CharField(max_length=15,null=True)
    address=models.TextField
    email=models.EmailField
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    phonenumber=models.CharField(max_length=10,null=True)
    age=models.PositiveSmallIntegerField
    profile_picture=models.ImageField

class Wallet(models.Model):    
   balance=models.IntegerField()
   currency=models.ForeignKey
   status=models.CharField(max_length=6,null=True)
   date=models.DateTimeField()
   amount=models.IntegerField()
   pin=models.PositiveSmallIntegerField()


class Receipt(models.Model):
    receiptdate=models.DateTimeField()
    Transaction=models.ForeignKey
    number=models.IntegerField
    file=models.FileField(max_length=15)
    receipttype=models.CharField
    amount=models.BigIntegerField  


class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=8,null=True)
    balance=models.IntegerField
    name=models.CharField(max_length=15)



class Transaction(models.Model):
    transaction_code=models.CharField(max_length=8,null=True) 
    wallet=models.ForeignObject
    transaction_amount=models.IntegerField(null=True)
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField(null=True)
    transactiondateandtime=models.DateTimeField(default=datetime.now)
    Receipt=models.OneToOneField(on_delete=models.CASCADE,to=Receipt)
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_a")
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_b")

class Card(models.Model):
    card_number=models.IntegerField(null=True)
    user_name=models.CharField(max_length=15,null=True)
    date_issue=models.DateTimeField(default=datetime.now)
    card_type=models.CharField(max_length=14,null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    Account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)



class Thirdparty(models.Model):
    name=models.CharField(max_length=15,null=True)
    account=models.ForeignKey(on_delete=models.CASCADE,to=Account,null=True)
    Phone_number=models.CharField(max_length=6,null=True)
    id=models.PositiveSmallIntegerField(primary_key=True)


class Notification(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    name=models.CharField(max_length=15,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=6)

class Loan(models.Model):
    loan_number=models.IntegerField(null=True)
    loan_type =models.CharField(max_length=32,null=True)
    amount=models.BigIntegerField(null=True)
    dateandtime=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Wallet)
    loanbalance=models.IntegerField(null=True)
    loanterm=models.IntegerField(null=True)
    payduedate=models.DateTimeField(default=datetime.now)

class Reward(models.Model):
    transaction=models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    Customer_id=models.IntegerField(null=True)
    description=models.TextField()
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    points=models.IntegerField(null=True) 

# Create your models here.
