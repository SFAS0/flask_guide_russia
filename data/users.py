import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.Text, sqlalchemy.ForeignKey('history_of_requests.user'), nullable=True)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    user = orm.relationship('HistoryOfRequests')

    def __repr__(self):
        return f'Пользователь - {self.login}(id:{self.id})'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
