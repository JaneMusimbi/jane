from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Wallet,Transaction


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display =("firstname","lastname","address","email")
    search_fields = ("first_name", "last_name")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display =("balance","currency","status","date","amount")
    search_fields = ("balance", "currency","status")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_number","password","balance")
    search_fields = ("account_number", "account_type")    
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display =("wallet","transaction_amount",)
    search_fields = ("wallet","transaction_amount")      
admin .site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display =("card_number","user_name","date_issue","card_type")
    search_fields = ("user_name","date_issue")  
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display =("name","account","phone_number","id")
    search_fields = ("name", "account","phone_number")  
admin.site.register(Thirdparty,ThirdpartyAdmin) 

class NotificationAdmin(admin.ModelAdmin):
    list_display =("id","name","date_and_time","status",)
    search_fields = ("id", "name","date_and_time",)  
admin.site.register(Notification) 

class ReceiptAdmin(admin.ModelAdmin):
    list_display =("receiptdate","receipttype")
    search_fields = (" receiptdate", "receipttype")  
admin.site.register(Receipt,ReceiptAdmin) 

class LoanAdmin(admin.ModelAdmin):
    list_display =("loan_number","loan_type","amount","date_and_time",)
    search_fields = ("loan_number", "loan_type","amount",)  
admin.site.register(Loan) 

class RewardAdmin(admin.ModelAdmin):
    list_display =("transaction","customer_id","description","gender",)
    search_fields = ("transaction", "customer_id","description",)  
admin.site.register(Reward) 