from app import db


def list_messages_by_chat(chat_id, limit):
    return db.query_all("""
        SELECT user_id, nick, name,
            message_id, content, added_at
        FROM Messages
        JOIN users USING (user_id)
        WHERE chat_id=%(chat_id)s
        ORDER BY added_at DESC
        LIMIT %(limit)s
    """, chat_id=int(chat_id), limit=int(limit))


def find_users(name):
    return db.query_all("""
        SELECT user_id, nick
        FROM Users
        WHERE name=%(name)s
        ORDER BY user_id
    """, name=name)


def find_user(nick):
    return db.query_one("""
        SELECT user_id, name
        FROM Users
        WHERE nick=%(nick)s
    """, nick=nick)


def create_personal_chat(topic):
    db.insert("""
	INSERT INTO Chats(is_group_chat, topic, last_message)
	VALUES (false, %(topic)s, 'create chat')
        """, topic=topic)
    db._commit_db('insert', 0)


def get_chats_list(nick):
    return db.query_all("""
        SELECT chat_id, topic 
        FROM Chats
	JOIN Members USING(chat_id)
	JOIN Users USING(user_id)
        WHERE Users.nick=%(nick)s
    """, nick=nick)


def get_chat_by_topic(topic):
    return db.query_one("""
        SELECT chat_id
        FROM Chats
        WHERE topic=%(topic)s
    """, topic=topic)


def send_message(nick, chat, content):
    user_id = str(find_user(nick)["user_id"])
    chat_id = str(get_chat_by_topic(chat)["chat_id"])
    db.insert("""
	INSERT INTO Messages(chat_id, user_id, content)
	VALUES (%(chat_id)s, %(user_id)s, %(content)s)
        """, chat_id=int(chat_id), user_id=int(user_id), content=content)
    db.insert("""
	UPDATE Members
	SET new_messages = %(message)s
	WHERE user_id = %(user_id)s
	AND chat_id = %(chat_id)s
        """, chat_id=int(chat_id), user_id=int(user_id), message=content)
    db._commit_db('insert', 0)


def get_message_id_by_content(content):
    return db.query_one("""
        SELECT message_id
        FROM Messages
        WHERE content=%(content)s
    """, content=content)


def read_message(nick, chat, content):
    user_id = str(find_user(nick)["user_id"])
    chat_id = str(get_chat_by_topic(chat)["chat_id"])
    message_id = str(get_message_id_by_content(content)["message_id"])
    print (message_id)
    db.insert("""
	UPDATE Members
	SET last_read_message_id = %(message_id)s
	WHERE user_id = %(user_id)s
	AND chat_id = %(chat_id)s
        """, chat_id=int(chat_id), user_id=int(user_id), message_id=int(message_id))
    db._commit_db('update', 0)
