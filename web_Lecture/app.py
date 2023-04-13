# app.py
from flask import Flask, render_template
from flask import request

import pymysql

# DB 연동
db_conn = pymysql.connect( # mysql와 연결해주는 'db_conn' 객체 생성
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'test',
    charset = 'utf8'
)

# 커서 객체 생성
cursor = db_conn.cursor() 
query = "select * from player"
cursor.execute(query)


for i in cursor: # cur
    print(i)

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 urlt
def index():
    temp = request.args.get('uid')
    temp1 = request.args.get('cid')

    print(temp,temp1)
    return render_template('index.html')

@app.route('/test',methods=['POST'])
def testpost():
    value = request.form['input']

    print(value)

    return render_template('postTest.html')

@app.route('/sqltest')
def sqltest():
    # 커서 객체 생성
    cursor = db_conn.cursor()
    query = "select * from player"
    cursor.execute(query)
    
    result = []
    print(cursor)
    for i in cursor: # i는 데이터의 1행
        temp = {'player_id':i[0],'player_name':i[1] }
        result.append(temp)
    
    return render_template('sqlTest.html', result_table = result)

@app.route('/detail')
def detailtest():
    temp = request.args.get('id')
    temp1 = request.args.get('name')

    # 커서 객체 생성
    cursor = db_conn.cursor()
    query = "select * from player where player_id = {} and player_name like '{}'".format(temp,temp1)
    cursor.execute(query)

    result = []
    for i in cursor:
        temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2],'weight':i[-1]}
        result.append(temp)
    
    return render_template('detail.html', result_table = result)
if __name__=="__main__":
    app.run(debug=True) # 스크립트 실행 시 가장 먼저 실행
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1",)d