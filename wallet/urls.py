from django.urls import path
from .views import register_account, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,register_card

# from .views import register_Transaction

urlpatterns=[
     path("register/",register_customer, name="registration"),
     path("wallet/",register_wallet, name="registration"),
     path("receipt/",register_receipt, name="registration"),
     path("account/",register_account, name="registration"),
     path("transaction/",register_transaction, name="registration"),
     path("card/",register_card, name="registration"),
     path("thirdparty/",register_thirdparty, name="registration"),
     path("notification/",register_notification, name="registration"),
     path("loan/",register_loan, name="registration"),
     path("reward/",register_reward, name="registration"),


]








     

     


     








