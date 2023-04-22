import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class District(SqlAlchemyBase):
    __tablename__ = 'district'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.Text)

    regs = orm.relationship('Regions', back_populates='dist_id')
