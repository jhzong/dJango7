from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.conf import settings
import json
from . import func_api

# ---------------------카카오페이api-----------------------------
# 상품 상세페이지
def detail(request):
    return render(request,'product/detail.html')

KAKAO_API_KEY=func_api.secret_key()# SECRET_KEY(dev)
KAKAOPAY_URL='https://open-api.kakaopay.com/online/v1/payment/ready'

# 카카오페이 준비단계
def prepare_payment(request):
    # # 상품정보를 (detail에서)가져옴
    # - 상품명:쟈뎅 오리지널 콜롬비아 페레이라 원두커피백 15p
    # - 판매가:4,330원
    # - 수량:1
    
    headers={
        'Authorization':f'SECRET_KEY {KAKAO_API_KEY}',
        'Content-Type': 'application/json',
    }
    # 결제정보
    data={
        "cid": "TC0ONETIME",                                    # 가맹점코드(test버전)
        "partner_order_id": "partner_order_id",                 # 가맹점 주문번호
		"partner_user_id": "partner_user_id",                   # 가맹점 회원 id
		"item_name": "쟈뎅 원두커피백",                           # 상품명
		"quantity": "1",                                        # 상품 수량
		"total_amount": "4330",                                 # 상품 총액
		"vat_amount": "433",                                    # 상품 부가세 금액
		"tax_free_amount": "0",                                 # 상품 비과세 금액
		"approval_url": "http://127.0.0.1:8000/product/approve", # 결제 성공 시 redirect url
		"fail_url": "http://127.0.0.1:8000/product/fail",        # 결제 실패 시 redirect url
		"cancel_url": "http://127.0.0.1:8000/product/cancel"     # 결제 취소 시 redirect url
    }
    
    # requests->url에 있는 데이터 전송,응답(프로그램 내부에서)
    # request,response->브라우저(http)에서 전달되는 객체
    response=requests.post(KAKAOPAY_URL,headers=headers,data=json.dumps(data,ensure_ascii=False))
    # 리턴받은 정보 - json으로 변환
    # =>결제 고유 번호,요청한 클라이언트가 (PC 웹/모바일 웹/모바일 앱)일 경우,결제 준비 요청 시간
    result=response.json()
    print('리턴받은결과 :',result)
    # session에 저장<=결제 고유 번호
    request.session['tid']=result['tid']
    request.session['order_id']=data['partner_order_id']
    
    # 결제창을 넘겨줌
    print('결제창 화면 : ',result['next_redirect_pc_url'])
    
    if response.status_code==200: # 결제성공 시
        return redirect(result['next_redirect_pc_url'])
    else:
        return redirect('/product/fail/')
    
# 결제승인 페이지
def approve(request):
    # 리턴받은 값
    pg_token=request.GET.get('pg_token')
    tid=request.session.get('tid')
    order_id=request.session.get('order_id')
    print('리턴받은 값 : ',pg_token, tid, order_id)
    # pg_token,tid 없으면 실패창으로
    if not pg_token or not tid:
        return redirect('/product/fail/')
    
    url='https://open-api.kakaopay.com/online/v1/payment/approve'    
    headers={
        'Authorization': f'SECRET_KEY {KAKAO_API_KEY}',
        'Content-Type': 'application/json',
    }
    data={
        "cid": "TC0ONETIME",
		"tid": tid,
		"partner_order_id": order_id,
		"partner_user_id": "partner_user_id",
		"pg_token": pg_token
    }
    response=requests.post(url,headers=headers,data=json.dumps(data,ensure_ascii=False))
    print('리턴받은 결과 : ',response)
    result=response.json()
    print('결제 날짜 : ',result.get("created_at"))
    
    if result.get('aid'):
        #db에 저장<=결제정보
        #결제정보models에 저장=>payment.object.create()
        print('결제 성공')
        return redirect('/product/success/')
    
    return redirect('/product/fail/')

# 결제성공 페이지
def success(request):
    return HttpResponse('결제성공 페이지')

# 결제실패 페이지
def fail(request):
    return HttpResponse('결제실패 페이지')

# 결제취소 페이지
def cancel(request):
    return HttpResponse('결제취소 페이지')