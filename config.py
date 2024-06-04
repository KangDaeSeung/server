import os

BASE_DIR =os.path.dirname(__file__)

SECRET_KEY ="dev" #os.urandom(24)
#SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:1234@localhost/study_flask'
SQLALCHEMY_TRACK_MODIFICATIONS=False
