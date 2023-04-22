from flask import Blueprint, jsonify
from data import db_session
from data.district import District


blueprint = Blueprint('federal_okrugs', __name__, template_folder='templates')


@blueprint.route('/api/federal_okrugs')
def federal_okrugs_api():
    db_sess = db_session.create_session()
    okrugs = {}
    for i in db_sess.query(District).all():
        okrugs[str(i.id)] = i.name
    return jsonify(okrugs)


