class BaseConfig:
    USER_DB='postgres'
    PASS_DB="contrasena1234"
    URL_DB='localhost'
    NAME_DB='bcrypt'
    FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI=FULL_URL_DB
    #SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="llave_secreta"
    DEBUG=False
    BCRYPT_LOG_ROUNDS=13
    SQLALCHEMY_TRACK_ODIFICATIONS=False
    print(SQLALCHEMY_DATABASE_URI)