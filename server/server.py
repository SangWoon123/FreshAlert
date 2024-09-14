from flask import Flask, request, jsonify
from models import db, Manager,Product,ProductName
from flask_cors import CORS
from datetime import datetime
from flask_migrate import Migrate
import os

app = Flask(__name__)


# CORS 설정
CORS(app, resources={r"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db.init_app(app)
migrate = Migrate(app, db)

#로그인 인증
@app.route("/login", methods=['POST'])
def manager_login():
    data = request.get_json()
    print(data)
    manager = Manager.query.filter_by(code=data['code']).first()

    if manager:
        return jsonify({'message': '인증성공'}), 200
    else:
        return jsonify({'message': '실패, 유효하지 않는 매니저 코드'}), 401
    

# 제품명 등록
@app.route('/product-name',methods=['POST'])
def add_product_name():
    data=request.get_json()
    new_product_name=ProductName(name=data['name'])
    db.session.add(new_product_name)
    db.session.commit()
    return jsonify({'message':'제품명등록 성공!'})

#제품명 조회
@app.route('/products-name',methods=['GET'])
def get_products_name():
    names=ProductName.query.all()
    return jsonify([{'id':n.id,'name':n.name} for n in names])

# 제품명 삭제
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_name = ProductName.query.get(id)
    if product_name:
        db.session.delete(product_name)
        db.session.commit()
        return jsonify({'message': '제품삭제 성공'})
    else:
        return jsonify({'message': '제품을 찾을 수 없습니다!'}), 404
    
# 제품 조회
@app.route('/products',methods=['GET'])
def get_products():
    today = datetime.now().date()
    products = Product.query.filter(Product.expiration > today).order_by(Product.expiration).all()
    return jsonify([{'id': p.id, 'name':p.product_name.name, 'quantity': p.quantity, 'expiration':p.expiration.strftime('%Y-%m-%d'),'checked':p.checked} for p in products])

# 제품 등록
@app.route('/product',methods=['POST'])
def add_product():
    data=request.get_json()
    new_product=Product(product_name_id=data['name_id'],quantity=data['quantity'],expiration=data['expiration'],created_at=datetime.now())
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message':'제품등록 성공!'})

# 제품삭제 추가


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)