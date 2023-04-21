import requests
from flask import Flask, redirect, render_template
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session, federal_okrugs_api, regions_api
from data.district import District
from data.geo_regions import Regions
from data.users import User
from forms.user_login import LoginForm
from forms.user_registration import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
def main():
    param = {'all_regs': new_dist, 'title': "Федеральные округа России"}
    return render_template('main_page.html', **param)


@app.route('/district/<okrug_name>')
def federal_okrugs(okrug_name):
    db_sess = db_session.create_session()
    dists = [dist.name for dist in db_sess.query(District).all()]
    regs_of_dist = []
    for i in range(8):
        regs_of_dist.append({dists[i]: [dist.name for dist in
                                        db_sess.query(Regions).filter(Regions.district_id == i + 1).all()]})
    regs = []
    for i in regs_of_dist:
        if okrug_name in i:
            regs = i[okrug_name]
    kon_regs = []
    regs.reverse()
    a = len(regs) / 4
    b = len(regs) // 4
    if a > b:
        a = b + 1
    else:
        a = b
    for i in range(a):
        if len(regs) > 4:
            kon_regs.append([regs.pop(), regs.pop(), regs.pop(), regs.pop()])
        else:
            regs.reverse()
            kon_regs.append([j for j in regs])
    param = {'all_regs': kon_regs}
    return render_template('regs_page.html', **param)


@app.route('/regions/<reg_name>')
def regions(reg_name):
    db_sess = db_session.create_session()
    reg_info = [reg.info for reg in db_sess.query(Regions).filter(Regions.name == reg_name).all()]
    response = requests.get(
        f'https://geocode-maps.yandex.ru/1.x/'
        f'?format=json&apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={reg_name}'
    )
    response = response.json()
    pos = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    pos = ','.join(pos.split())
    response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={pos}&size=650,450&z=5&l=map')
    with open('static/img/map.jpeg', mode='wb') as map_file:
        map_file.write(response.content)
    param = {'reg_info': reg_info[0], 'reg_name': reg_name,
             'map': 'img/map.jpeg'
             }
    return render_template('info_reg.html', **param)


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
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=True)
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/register")


if __name__ == '__main__':
    db_session.global_init('db/regions_and_users.db')
    db = db_session.create_session()
    districts = sorted([dist.name for dist in db.query(District).all()])
    new_dist = [districts[:3], districts[3:6], districts[6:]]
    app.register_blueprint(federal_okrugs_api.blueprint)
    app.register_blueprint(regions_api.blueprint)
    app.run(port=8080, host='127.0.0.1')
