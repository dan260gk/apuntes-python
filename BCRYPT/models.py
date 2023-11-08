import jwt
import datetime
from config import BaseConfig
from app import db,bcrypt

class User(db.Model):
    __tablename__="users"
    id=db.Colum(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.string(255),unique=True,nullable=False)
    password=db.Column(db.string(255),nullable=False)
    registered_on=db.Column(db.Datetime,nullable=False)
    admin=db.Column(db.Boolean, nullable=False,default=False)

    def __init__(self,email,password,admin=False) -> None:
        self.email=email
        self.password=bcrypt.generate_password_hash(
            password,BaseConfig.BCRYPT_LOG_ROUNDS
        ).decode()

        self.registered_on=datetime.datetime.now()
        self.admin=admin

    def encode_auth_token(self,user_id):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=5),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id
            }

            return jwt.encode(
                payload,
                BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, BaseConfig.SECRET_KEY,algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError as e:
            return 'Signature Expired Please log in again'
        except jwt.InvalidTokenError as e:
            return 'Invalid token'
