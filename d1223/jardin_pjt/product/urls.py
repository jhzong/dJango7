
from django.urls import path,include
from . import views

app_name='product'
urlpatterns = [
    path('detail/',views.detail,name='detail'),
    # 결제요청화면
    path('prepare_payment/',views.prepare_payment,name='prepare_payment'),# 결제요청창
    # 결제후화면
    path('approve/',views.approve,name='approve'),# 결제승인창
    path('success/',views.success,name='success'),# 결제완료창
    path('fail/',views.fail,name='fail'),
    path('cancel/',views.cancel,name='cancel'),
]
