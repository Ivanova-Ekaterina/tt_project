from flask import request, jsonify
from app import app, isonrpc
from app import model


@app.route('/messages/', methods=['GET'])
def messages():
    chat_id = int(request.args.get('chat_id'))
    limit = int(request.args.get('limit'))
    messages = model.list_messages_by_chat(chat_id, limit)
    resp = jsonify(messages)
    resp.status_code = 200
    mimetype='application/json'
    return resp

@app.route('/find_user/', methods=['GET'])
def find_user():
    nick = request.args.get('nick')
    user = model.find_user(nick)
    resp = jsonify(user)
    resp.status_code = 200
    mimetype='application/json'
    return resp

@app.route('/find_users/', methods=['GET'])
def find_users():
    name = request.args.get('name')
    users = model.find_users(name)
    resp = jsonify(users)
    resp.status_code = 200
    mimetype='application/json'
    return resp

@app.route('/get_chats_list/', methods=['GET'])
def get_chats_list():
    nick = request.args.get('nick')
    chats = model.get_chats_list(nick)
    resp = jsonify(chats)
    resp.status_code = 200
    mimetype='application/json'
    return resp

@app.route('/create_personal_chat/', methods=['POST'])
def create_personal_chat():
    topic = 'test'
    model.create_personal_chat(topic)
    resp = jsonify('')
    resp.status_code = 204
    mimetype='application/json'
    return resp

@isonrpc.method('get_messages')
def messages_rpc(limit, chat_id):
    return model.list_messages_by_chat(chat_id, limit)

@isonrpc.method('find_user')
def find_user_rpc(nick):
    return model.find_user(nick)
    
@isonrpc.method('find_users')
def find_user_rpc(name):
    return model.find_users(name)

@isonrpc.method('get_chats_list')
def find_user_rpc(nick):
    return model.get_chats_list(nick)

@isonrpc.method('create_personal_chat')
def find_user_rpc(topic):
    return model.create_personal_chat(topic)

@isonrpc.method('send_message')
def send_message_rpc(nick, chat, content):
    return model.send_message(nick, chat, content)

@isonrpc.method('read_message')
def read_message_rpc(nick, chat, content):
    return model.read_message(nick, chat, content)

