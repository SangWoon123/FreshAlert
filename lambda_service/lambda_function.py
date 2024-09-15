# 로직
# 매일 오후 6시 스케줄링으로 오늘날짜 기준 + 1일 날짜에 해당하는 제품류별로 카운팅
  # DB에서 오늘 날짜 + 1일 에 해당하는 데이터 수집
  # 수집된 데이터를 가지고 종류별 카운팅

from datetime import datetime,timedelta
from sms_service import send_sms_message
from database import get_products_next_day
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_expiration_message(event,context):
  # 유통기한 계산
  try:
    products=get_products_next_day()
    # 메시지 작성
    # [유통기한] 2024년 9월 11일 
    #  - [서울우유] 초코우유 500ml 4개 (제품명, 개수)
    tomrrow=datetime.now().date()+timedelta(days=1)
    message=f"[유통기한] {tomrrow.strftime('%Y년 %m월 %d일')}\n"

    for product in products:
      message+=f"    - {product['name']} {product['quantity']}개\n"

    return message
  except Exception as e:
    logger.error('DB에서 오류 발생: %s', e)
    return None


# 람다 핸들러
def lambda_handler(event, context):
    message = generate_expiration_message(event,context)
    if message:
        send_sms_message(message)
    else:
       logger.info('not working time')
       return
  

  
    

