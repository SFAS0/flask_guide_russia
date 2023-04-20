import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Regions(SqlAlchemyBase):
    __tablename__ = 'geo_regions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    district_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('district.id'), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    info = sqlalchemy.Column(sqlalchemy.Text)

    dist_id = orm.relationship('District')
