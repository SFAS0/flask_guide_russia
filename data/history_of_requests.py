from datetime import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class HistoryOfRequests(SqlAlchemyBase):
    __tablename__ = 'history_of_requests'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    link = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    history = orm.relationship('User', back_populates='user')
