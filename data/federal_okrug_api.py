from flask import Blueprint, jsonify
from data import db_session
from data.district import District


blueprint = Blueprint('federal_okrug', __name__, template_folder='templates')


@blueprint.route('/api/federal_okrug/<int:okrug_id>')
def federal_okrug_api(okrug_id):
    db_sess = db_session.create_session()
    okrugs = {}
    for i in db_sess.query(District).all():
        if i.id == okrug_id:
            okrugs[str(i.id)] = i.name
    return jsonify(okrugs)


