# app.py
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/') # 접속하는 urlt
def index():
   
    return render_template('index.html')

@app.route('/index2') # 접속하는 urlt
def index2():
   
    return render_template('index2.html')

@app.route('/index4') # 접속하는 urlt
def index4():
   
    return render_template('index4.html')

@app.route('/index5') # 접속하는 urlt
def index5():
   
    return render_template('index5.html')

if __name__=="__main__":    # 스크립트 실행 시 가장 먼저 실행
    app.run(debug=True) 