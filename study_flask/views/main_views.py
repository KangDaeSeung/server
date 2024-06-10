from flask import Blueprint, url_for
from werkzeug.utils import redirect

import pymysql.cursors


from datetime import datetime

bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/test')
def test():
    return '어서와 플라스크는 처음이지!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))



@bp.route('/test1/')
def test1():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='study_flask',
                             cursorclass=pymysql.cursors.DictCursor)
    sql = "INSERT INTO question (subject, content, create_date) VALUES (%s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, ('테스트1', '테스트용 질문', datetime.now()))
    connection.commit()
    connection.close()
    return 'OK'

    
