from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Manager(db.Model):
  __tablename__ = 'manager'
  id = db.Column(db.Integer, primary_key=True)
  code=db.Column(db.Integer,unique=True)


class ProductName(db.Model):
    __tablename__ = 'product_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False) 
    products = db.relationship('Product', backref='product_name', lazy=True) 

class Product(db.Model):
  __tablename__='product'
  id=db.Column(db.Integer,primary_key=True)
  product_name_id = db.Column(db.Integer, db.ForeignKey('product_name.id'), nullable=False)  # 외래키 설정
  quantity=db.Column(db.Integer)
  expiration = db.Column(db.Date)  # 날짜 형식 (2024-10-25)으로 저장
  checked=db.Column(db.Boolean,default=False)
  created_at = db.Column(db.DateTime, default=datetime) 
  deleted_at = db.Column(db.DateTime, nullable=True)  


  