from app import db
from datetime import datetime


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nick = db.Column(db.String(50), nullable=False, unique=True)
    avatar = db.Column(db.String(50), nullable=True)
    members = db.relationship('Member', backref='user', lazy = True)
    messages = db.relationship('Message', backref='user', lazy = True)

    def __init__(self, name, nick):
        self.name = name
        self.nick = nick


class Member(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'), nullable=False)
    member_id = db.Column(db.Integer, primary_key=True)
    new_messages = db.Column(db.String(50), nullable=False)
    last_read_message_id = db.Column(db.Integer, db.ForeignKey('message.message_id'), nullable=True)

    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.new_messages = 'add'


class Chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    is_group_chat = db.Column(db.Boolean)
    topic = db.Column(db.String(50), nullable=False, unique=True)
    last_message = db.Column(db.String(50), nullable=False)
    members = db.relationship('Member', backref='chat', lazy = True)
    messages = db.relationship('Message', backref='chat', lazy=True)

    def __init__(self, topic, is_group):
        self.topic = topic
        self.is_group_chat = is_group
        self.last_message = 'insert'


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    chat_id =  db.Column(db.Integer, db.ForeignKey('chat.chat_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    added_at = db.Column(db.DateTime)
    last_read_messages = db.relationship('Member', backref='last_read', lazy = True)

    def __init__(self, chat_id, user_id, content):
        self.chat_id = chat_id
        self.user_id = user_id
        self.content = content
        self.added_at = datetime.today()


