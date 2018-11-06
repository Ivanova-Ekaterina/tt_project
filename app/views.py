from flask import request, abort, jsonify, json, Response

from app import app


@app.route('/')
def index(name="World"):
    return "Hello, {}".format(name)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/login/">
            <input name="full_name">
            <input name="user_nickname">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        resp = jsonify(request.form)
        resp.status_code = 200
        return resp


@app.route('/find_user/', methods=['GET', 'POST'])
def find_user():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/find_user/">
            <input name="full_name">
            <input name="user_nickname">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        resp = jsonify(request.form)
        resp.status_code = 200
        return resp


@app.route('/find_chat/', methods=['GET', 'POST'])
def find_chat():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/find_chat/">
            <input name="chat_name">
            <input name="chat_nickname">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        resp = jsonify(request.form)
        resp.status_code = 200
        return resp


@app.route('/get_chats_list/', methods=['GET'])
def get_chats_list():

    data = {
            'name': ['first', 'second'],
            'nick_name': ['tt', '516'],
            'participant': [5, 8]
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')

    return resp


@app.route('/create_private_chat/', methods=['POST'])
def create_private_chat():

    data = {
            'name': 'new private chat'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/create_group_chat/', methods=['POST'])
def create_group_chat():

    data = {
        'name': 'new group chat'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/add_users_to_chat/', methods=['POST'])
def add_users_to_chat():

    data = {
        'name': 'add user'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/leave_chat/', methods=['POST'])
def leave_chat():

    data = {
            'name': 'leave chat'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/send_message/', methods=['POST'])
def send_message():

    data = {
            'name': 'send message'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')

    return resp


@app.route('/read_message/', methods=['GET'])
def read_message():

    data = {
            'user': 'kate',
            'text': 'hello',
            'time': ''
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/load_file/', methods=['POST'])
def load_file():

    data = {
            'name': 'new file'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
