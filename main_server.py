from flask import Flask, url_for, request, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

from data import db_session
from data.users import User
from data.history_of_requests import HistoryOfRequests
from data.district import District
from data.geo_regions import Regions
from forms.user_registration import RegisterForm
from forms.user_login import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class MainPage(FlaskForm):
    submit = SubmitField('regions')


@app.route('/', methods=['GET', 'POST'])
def main():
    param = {'all_regs': new_dist}
    return render_template('main_page.html', **param)
    # href="{url_for('static', filename='css/style.css')}">


@app.route('/regions/<reg_name>')
def roots(reg_name):
    return f'{reg_name}'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        user = User(
            login=form.login.data,
            password=form.password.data
        )
        user.set_password(form.password.data)
        db.add(user)
        db.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    # не готово
    render_template('login.html', title='Авторизация', form={})


if __name__ == '__main__':
    db_session.global_init('db/regions_and_users.db')
    db = db_session.create_session()
    districts = sorted([dist.name for dist in db.query(District).all()])
    new_dist = [districts[:3], districts[3:6], districts[6:]]
    app.run(port=8080, host='127.0.0.1')
