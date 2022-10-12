
from django.db import router
from django.urls import path,include
from rest_framework import routers

from api.serializer import Accountserializer, Cardserializer, Loanserializer, Notificationserializer, Receiptserializer, Transactionserializer, Walletserializer
from .views import Customerviewsets

router = routers.DefaultRouter()
router.register ( r"customer" ,Customerviewsets)
router.register( r"wallet" ,Walletserializer)
router.register( r"account" ,Accountserializer)
router.register( r"card" ,Cardserializer)
router.register( r"transaction" ,Transactionserializer)
router.register( r"loan" , Loanserializer)
router.register( r"receipt" , Receiptserializer)
router.register( r"notification" , Notificationserializer)

urlpatterns= [
    path("",include(router.urls)),

]