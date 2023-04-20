from datetime import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class HistoryOfRequests(SqlAlchemyBase):
    __tablename__ = 'history_of_requests'

    user = sqlalchemy.Column(sqlalchemy.Text, nullable=True, primary_key=True)
    time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    link = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    history = orm.relationship('User', back_populates='user')
