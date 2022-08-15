from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Wallet,Transaction


# Register your models here.
admin.site.register(Customer)
admin.site.register(Wallet)    
admin.site.register(Account)     
admin .site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty) 
admin.site.register(Notification) 
admin.site.register(Receipt) 
admin.site.register(Loan) 
admin.site.register(Reward) 