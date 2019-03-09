from flask import request, jsonify, redirect
from app import app, isonrpc, cache
from app import model
import requests
import json
from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.cache import SimpleCache

def calculate_value(item, user_id):
    if (item == 'get_chats_list'):
        return model.get_chats_list(user_id)


@app.route('/')
def index(name="World"):
    auth_code = request.args.get('code')
    response = requests.get('https://oauth.vk.com/access_token?'
                     + 'client_id=6748743'
                     + '&client_secret=Zbuk3KaKrXB9og8JyG18'
                     + '&redirect_uri=http://127.0.0.1:5000/'
                     + '&code=' + auth_code)
    response_obj = json.loads(response.text)
    print(response_obj['access_token'])
    return "Hello, {}".format(name)

@app.route('/auth/')
def auth():
    return redirect("https://oauth.vk.com/authorize?client_id=6748743" +
                    "&display=page" +
                    "&redirect_uri=http://127.0.0.1:5000/" +
                    "&response_type=code" +
                    "&v=5.92", code=302)

def get_my_item(item, user_id):
    rv = cache.get(item + user_id)
    if rv is None:
        rv = calculate_value(item, user_id)
        cache.set(item, rv, timeout=5 * 60)
        print ("from method")
    else:
        print("from cache")
    return rv

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
    chats = get_my_item('get_chats_list', nick) #model.get_chats_list(nick)
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

