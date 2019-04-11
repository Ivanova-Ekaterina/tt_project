from .model import Chat, User, Message, Member
from flask import request, abort, jsonify, json, Response, redirect
from app import app, db
from .db import *
from .task import send_create_chat

#@app.route('/')
#def index(name="World"):
#    auth_code = request.args.get('code')
#    print(auth_code)
#    return "Hello, {}".format(name)

@app.route('/API/create_chat_form/', methods=['GET', 'POST'])
def create_chat_f():
    if request.method == "GET":
        return """<html><head></head><body>
    <form method="POST" action="/API/create_chat_form/">
    <input placeholder="topic" name="topic" >
    <input name="is_group_chat" type="checkbox" >
    <input type="submit" >
    </form>
    </body></html>"""
    else:
        resp = request.form
        form = ChatForm(resp)
        if form.validate():
            if (resp.get("is_group_chat")):
                chat = create_gr_chat(resp.get("topic"))
            else:
                chat = create_pr_chat(resp.get("topic"))
#            send_create_chat.delay(resp.get("topic"))
            return chat
        else:
            return "Check your data, because: {}. ".format(form.errors)


@app.route('/API/create_user_form/',  methods=['GET', 'POST'])
def create_user_f():
    if request.method == "GET":
        return """<html><head></head><body>
       <form method="POST" action="/API/create_user_form/">
       <input placeholder="name" name="name" >
       <input placeholder="nick" name="nick" >
       <input type="submit" >
       </form>
       </body></html>"""
    else:
        resp = request.form
        form = UserForm(resp)
        if form.validate():
            user = create_u(resp.get("nick"), resp.get("name"))
            return user
        else:
            return "Check your data, because: {}. ".format(form.errors)
    return


@app.route('/API/create_private_chat/<string:topic>')
def create_chat(topic):
    chat = create_pr_chat(topic)
    send_create_chat.delay(topic)
    return str(chat)


@app.route('/API/create_group_chat/<string:topic>')
def create_group_chat(topic):
    chat = create_gr_chat(topic)
 #   send_create_chat.delay(topic)
    return str(chat)


@app.route('/API/create_user/<string:nick>&<string:name>')
def create_user(nick, name):
    user = create_u(nick, name)
    return str(user)


@app.route('/API/add_users_to_chat/<int:chat>&<int:user>')
def add_user(chat, user):
    member = add_u(chat, user)
    return str(member)


@app.route('/API/send_message/<int:chat>&<int:user>&<string:content>')
def send_message(user, chat, content):
    mes = send_ms(user, chat, content)
    return str(mes)


@app.route('/API/find_user/<string:nick>')
def find_user(nick):
    user = get_user(nick)
    return str(user)


@app.route('/API/find_chat/<string:topic>')
def find_chat(topic):
    chat = get_chat(topic)
    return str(chat)


@app.route('/API/get_chats_list')
def get_chat_list():
    chats = get_chats()
    return str(chats)


@app.route('/API/find_all_chats_for_user/<string:nick>')
def get_chat_list_for_user(nick):
    chats = get_all_chats(nick)
    return str(chats)


@app.route('/API/read_message/<int:message_id>&<string:topic>&<string:nick>')
def read(nick, topic, message_id):
    read = read_ms(topic, nick, message_id)
    return str(read)


@app.route('/API/leave_chat/<string:topic>&<string:nick>')
def leave_from_chat(topic, nick):
    delete = delete_member(topic, nick)
    return str(delete)

@app.route('/API/create_chat_with_user/<string:topic>&<string:nick1>&<string:nick2>')
def create_chat_with_user(topic, nick1, nick2):
    create = create_pr_chat(topic);
    nick1 = find_user(nick1)
    nick2 = find_user(nick2)
    print (create)
   # add_u(chat, nick1) #int
   # add_u(chat, nick2) #int
    return str(create)

@app.route('/API/auth/')
def auth():
    return
