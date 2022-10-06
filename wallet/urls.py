from django.urls import path
from .views import Account_profile, Card_profile, Customer_profile, Receipt_profile, Transaction_profile, Wallet_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_account, list_card, list_customer, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, register_account, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,register_card

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
     path("customers/",list_customer,name="registration"),
     path("wallets/",list_wallet,name="registration"),
     path("receipts/",list_receipt,name="registration"),
     path("accounts/",list_account,name="registration"),
     path("transactions/",list_transaction,name="registration"),
     path("cards/",list_card,name="registration"),
     path("thirdparts/",list_thirdparty,name="registration"),
     path("notifications/",list_notification,name="registration"),
     path("loans/",list_loan,name="registration"),
     path("rewards/",list_reward,name="registration"),

     path("customers/<int:id>/",Customer_profile, name="customer_profile"),
     path("customers/edit/<int:id>/", edit_profile, name="edit_profile"),

     path("wallets/<int:id>/",Wallet_profile, name="wallet_profile"),
     path("wallets/edit/<int:id>/", edit_wallet, name="edit_wallet"),

     path("accounts/<int:id>/",Account_profile, name="account_profile"),
     path("accounts/edit/<int:id>/", edit_account, name="edit_account"),

     path("cards/<int:id>/",Card_profile, name="card_profile"),
     path("cards/edit/<int:id>/", edit_card, name="edit_card"),

     path("transactions/<int:id>/",Transaction_profile, name="transaction_profile"),
     path("transactions/edit/<int:id>/", edit_transaction, name="edit_transaction"),


     path("receipts/<int:id>/",Receipt_profile, name="receipt_profile"),
     path("receipts/edit/<int:id>/", edit_receipt, name="edit_receipt"),
]










     

     


     








