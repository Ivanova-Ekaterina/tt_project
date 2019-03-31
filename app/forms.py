from wtforms import validators, Form, TextField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length
from .model import User, Chat

class UserForm(Form):
    name = TextField ('name', validators=[DataRequired(), Length(max=30)])
    nick = TextField('nick', validators=[DataRequired(), Length(max=25)])

class ChatForm(Form):
    topic = TextField('topic', validators=[DataRequired(), Length(max=20)])
    is_group_chat = BooleanField('is_group_chat')