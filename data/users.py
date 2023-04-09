import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.Text, sqlalchemy.ForeignKey('history_of_requests.user'), nullable=True)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    user = orm.relationship('HistoryOfRequests')
