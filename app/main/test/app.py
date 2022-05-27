# -*- coding: utf-8 -*-
# Description:
# Created: jjunf 2021/8/22 16:37
import datetime

from flask import Flask, render_template, request
from werkzeug.utils import redirect

import settings
from service import UserService

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        pass_word = request.form.get('pass_word')
        create_date = datetime.datetime.now()
        user = {'user_name': user_name, 'pass_word': pass_word, 'create_date': create_date}
        print(user)
        UserService().register_service(user)
        return redirect('index')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(port=5000)
