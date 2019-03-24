from .model import Chat, User, Message, Member
from app import app, db

@app.route('/create_private_chat/<string:topic>')
def create_chat(topic):
    chat = Chat(topic, False)
    db.session.add(chat)
    db.session.commit()
    return topic


@app.route('/create_group_chat/<string:topic>')
def create_group_chat(topic):
    chat = Chat(topic, True)
    db.session.add(chat)
    db.session.commit()
    return topic


@app.route('/create_user/<string:nick>&<string:name>')
def create_user(nick, name):
    user = User(name, nick)
    db.session.add(user)
    db.session.commit()
    return nick

@app.route('/add_users_to_chat/<int:chat>&<int:user>')
def add_user(chat, user):
    member = Member(chat, user)
    db.session.add(member)
    db.session.commit()
    return 'ok'

@app.route('/send_message/<int:chat>&<int:user>&<string:content>')
def send_message(user, chat, content):
    message = Message(chat, user, content)
    db.session.add(message)
    db.session.commit()
    return content