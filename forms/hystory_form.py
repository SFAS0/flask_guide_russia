from flask_wtf import FlaskForm
from wtforms import SubmitField


class HistoryForm(FlaskForm):
    submit = SubmitField('Главная страница')
