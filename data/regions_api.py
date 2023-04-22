from flask import Blueprint, jsonify
from data import db_session
from data.geo_regions import Regions


blueprint = Blueprint('regions_api', __name__, template_folder='templates')


@blueprint.route('/api/regions_api')
def regions():
    db_sess = db_session.create_session()
    regs = {}
    for i in db_sess.query(Regions).all():
        regs[i.name] = {'id': i.id, 'district_id': i.district_id, 'info': i.info}
    return jsonify(regs)


