# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    path = '/'
    all_file = os.listdir(path)
    return render_template('login.html', all_file=all_file)


@app.route('/login', methods=['GET','POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    if name == 'admin' and password == 'admin':
        return render_template('index.html', name=name)
    return render_template('index.html', name=name)


@app.route('/console', methods=['GET','POST'])
def console():
    if request.method == 'POST':
        return '接收数据，待处理数据'
    return render_template('console.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/operaterule', methods=['GET'])
def operaterule():
    return render_template('operaterule.html')

@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='2333')
