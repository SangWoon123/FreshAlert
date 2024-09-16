import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# CORS 설정
CORS(app, resources={r"*": {"origins": "*"}})

# MySQL 데이터베이스 연결
def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASS'),
        db=os.environ.get('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )


# 로그인 인증
@app.route("/login", methods=['POST'])
def manager_login():
    data = request.get_json()
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM manager WHERE code = %s"
            cursor.execute(sql, (data['code'],))
            manager = cursor.fetchone()

        if manager:
            return jsonify({'message': '인증성공'}), 200
        else:
            return jsonify({'message': '실패, 유효하지 않는 매니저 코드'}), 401
    finally:
        connection.close()

# 제품명 등록
@app.route('/product-name', methods=['POST'])
def add_product_name():
    data = request.get_json()
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO product_name (name) VALUES (%s)"
            cursor.execute(sql, (data['name'],))
        connection.commit()
        return jsonify({'name': data['name']})
    finally:
        connection.close()

# 제품명 조회
@app.route('/products-name', methods=['GET'])
def get_products_name():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name FROM product_name"
            cursor.execute(sql)
            names = cursor.fetchall()
        return jsonify(names)
    finally:
        connection.close()

# 제품명 삭제
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 1. 해당 제품명(id)을 참조하는 모든 제품을 먼저 삭제
            delete_products_sql = "DELETE FROM product WHERE product_name_id = %s"
            cursor.execute(delete_products_sql, (id,))
            
            # 2. 이제 product_name을 삭제
            delete_product_name_sql = "DELETE FROM product_name WHERE id = %s"
            cursor.execute(delete_product_name_sql, (id,))
        connection.commit()
        if cursor.rowcount > 0:
            return jsonify({'message': '제품삭제 성공'})
        else:
            return jsonify({'message': '제품을 찾을 수 없습니다!'}), 404
    finally:
        connection.close()

# 제품 조회
@app.route('/products', methods=['GET'])
def get_products():

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT p.id, pn.name, p.quantity, p.expiration, p.checked 
            FROM product p 
            JOIN product_name pn ON p.product_name_id = pn.id 
            WHERE p.expiration > curdate()
            ORDER BY p.expiration
            """
            cursor.execute(sql)
            products = cursor.fetchall()
        return jsonify([{
            'id': p['id'],
            'name': p['name'],
            'quantity': p['quantity'],
            'expiration': p['expiration'].strftime('%Y-%m-%d'),
            'checked': p['checked']
        } for p in products])
    finally:
        connection.close()

# 제품 등록
@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO product (product_name_id, quantity, expiration, created_at) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['name_id'],
                data['quantity'],
                data['expiration'],
                datetime.now()
            ))
        connection.commit()
        return jsonify({'message': '제품등록 성공!'})
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)