import pymysql
import os
import pymysql.cursors
from datetime import datetime,timedelta


# RDS 연결
def db_connection():
  #커넥션 정보
  connection=pymysql.connect(
     host=os.environ['HOST'],
     port=int(os.environ.get('PORT', 3306)),
     user=os.environ['USER'],
     password=os.environ['PASSWORD'],
     database=os.environ['DATA_BASE'],
     charset='utf8mb4',
     cursorclass=pymysql.cursors.DictCursor # 쿼리 결과 딕셔너리 형태로 변환
  )

  return connection

# 다음날짜 제품(Product) 정보 가져오기
def get_products_next_day():
  # 날짜
  tomrrow=datetime.now().date()+timedelta(days=1)

  connection=db_connection()
  # SQL
  try:
    with connection.cursor() as cursor:
      sql="""
      SELECT p.id, pn.name, p.quantity, p.expiration 
      FROM product p
      JOIN product_name pn ON p.product_name_id = pn.id
      WHERE p.expiration = %s
      """
      cursor.execute(sql,(tomrrow,))
      result=cursor.fetchall()
      print(f"쿼리 결과: {result}")  # 디버깅용 출력
      return result
  finally:
    connection.close()
