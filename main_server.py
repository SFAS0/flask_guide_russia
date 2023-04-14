from flask import Flask, url_for, request, redirect, render_template

from data import db_session
from data.users import User
from data.history_of_requests import HistoryOfRequests
from data.district import District
from data.geo_regions import Regions


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def main():
    param = {'all_regs': new_dist}
    return render_template('main_page.html', **param)
    # href="{url_for('static', filename='css/style.css')}">


@app.route('/regions/<reg_name>')
def roots(reg_name):
    param = {'regname': reg_name, 'regimg': 'https://static-maps.yandex.ru/1.x/?ll=30.458673,59.898065&size=650,450&z=7&l=map'}
    return render_template('info_regs.html', **param)


if __name__ == '__main__':
    db_session.global_init('db/regions_and_users.db')
    db = db_session.create_session()
    districts = sorted([dist.name for dist in db.query(District).all()])
    new_dist = [districts[:3], districts[3:6], districts[6:]]
    app.run(port=8080, host='127.0.0.1')
