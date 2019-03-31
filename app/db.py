import flask
import psycopg2
from app import db
from .model import *
from .forms import *


def get_user(nick):
    user = User.query.filter_by(nick=nick).first()
    return str(user)


def get_chat(topic):
    chat = Chat.query.filter_by(topic=topic).first()
    return str(chat)


def get_chats():
    chats = Chat.query.all()
    return str(chats)


def get_all_chats(nick):
    chats = Chat.query.join(Member).join(User).filter_by(nick=nick).all()
    return str(chats)


def read_ms(topic, nick, message_id):
    message = Member.query.join(User).join(Chat).filter(User.nick==nick, Chat.topic==topic).first()
    message.last_read_message_id = message_id
    db.session.commit()
    return str(message)


def delete_member(topic, nick):
    delete = Member.query.join(User).join(Chat).filter(User.nick == nick, Chat.topic == topic).first()
    db.session.delete(delete)
    db.session.commit()
    return str(delete)


def send_ms(user, chat, content):
    message = Message(chat, user, content)
    db.session.add(message)
    db.session.commit()
    return str(message)


def add_u(chat, user):
    member = Member(chat, user)
    db.session.add(member)
    db.session.commit()
    return str(member)


def create_u(nick, name):
    user = User(name, nick)
    db.session.add(user)
    db.session.commit()
    return str(user)


def create_gr_chat(topic):
    chat = Chat(topic, True)
    db.session.add(chat)
    db.session.commit()
    return str(chat)


def create_pr_chat(topic):
    chat = Chat(topic, False)
    db.session.add(chat)
    db.session.commit()
    return str(chat)