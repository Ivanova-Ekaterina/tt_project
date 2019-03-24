from unittest import TestCase
import psycopg2
from app import app
from app.config import ProductionConfig, TestingConfig
import json
import postgresql
from datetime import datetime


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """DROP TABLE attachments""",
        """DROP TABLE members""",
        """DROP TABLE messages""",
        """DROP TABLE users""",
        """DROP TABLE chats""",
        """
       CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name text NOT NULL,
            nick text NOT NULL,
            avatar text
            )
        """,
        """ 
        CREATE TABLE chats (
            chat_id SERIAL PRIMARY KEY,
            is_group_chat boolean,
            topic text NOT NULL,
            last_message text NOT NULL
            )
        """,
        """
        CREATE TABLE messages (
            message_id SERIAL PRIMARY KEY,
            chat_id INTEGER REFERENCES chats(chat_id),
            user_id INTEGER REFERENCES users(user_id),
            content text NOT NULL,
            added_at timestamp NOT NULL
            )
        """,
        """
        CREATE TABLE attachments (
            attach_id SERIAL PRIMARY KEY,
	        message_id INTEGER REFERENCES messages(message_id),
	        chat_id INTEGER REFERENCES chats(chat_id),
	        user_id INTEGER REFERENCES users(user_id),
            type text NOT NULL,
            url text NOT NULL
            )
        """,
        """
        CREATE TABLE members (
            member_id SERIAL PRIMARY KEY,
	        chat_id INTEGER REFERENCES chats(chat_id),
	        user_id INTEGER REFERENCES users(user_id),
            new_messages text NOT NULL,
	        last_read_message_id INTEGER REFERENCES messages(message_id)
            )
        """
    )

    conn = None
    try:
        # read the connection parameters
        #   params = app.config.TestingConfig()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            database=TestingConfig.DB_NAME, host=TestingConfig.DB_HOST,
            user=TestingConfig.DB_USER, password=TestingConfig.DB_PASS)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def generate():
    create_tables()
    with postgresql.open('pq://ekaterina:@localhost/track_test') as db:
        ins = db.prepare("INSERT INTO users (nick, name) VALUES ($1, $2)")

        ins("Tina", "Margarita Miller")
        ins("Chris", "Cristopher Smith")
        ins("Al", "Albert Johnson")
        ins("Polly", "Paula Brown")
        ins("Eddy", "Edgar Davis")

        ins = db.prepare("INSERT INTO chats (is_group_chat, topic, last_message) VALUES ($1, $2, $3)")

        ins(False, "tt", "Hi!")
        ins(False, "kvant", "Bye")
        ins(False, "mipt", "Message 10")
        ins(False, "intel", "Test 10")
        ins(False, "home", "J")

        ins = db.prepare("INSERT INTO members (chat_id, user_id, new_messages) VALUES ($1, $2, $3)")

        ins(1, 1, "Good morning!")
        ins(1, 2, "Hi!")
        ins(2, 1, "Good")
        ins(2, 3, "Bye")
        ins(3, 2, "Message 10")
        ins(3, 4, "Message 9")
        ins(4, 4, "Test 10")
        ins(4, 5, "Test 9")
        ins(5, 3, "J")
        ins(5, 5, "I")

        ins = db.prepare("INSERT INTO messages (chat_id, user_id, content, added_at) VALUES ($1, $2, $3, $4)")

        ins(1, 1, 'Hello!', datetime(2019, 3, 9))
        ins(1, 1, 'How are you?', datetime(2019, 3, 9))
        ins(1, 2, 'Better tnan you', datetime(2019, 3, 9))
        ins(1, 1, 'Ok', datetime(2019, 3, 9))
        ins(1, 2, 'What is the news?', datetime(2019, 3, 9))
        ins(1, 1, 'Nothing', datetime(2019, 3, 9))
        ins(1, 2, 'Bye', datetime(2019, 3, 9))
        ins(1, 1, 'Goodbye', datetime(2019, 3, 9))
        ins(1, 2, 'Good morning!', datetime(2019, 3, 10))
        ins(1, 1, 'Hi!', datetime(2019, 3, 10))

        ins(2, 1, 'Hi!', datetime(2019, 3, 8))
        ins(2, 3, 'Hello!', datetime(2019, 3, 8))
        ins(2, 3, 'How is the weather?', datetime(2019, 3, 8))
        ins(2, 1, 'Good.', datetime(2019, 3, 8))
        ins(2, 3, 'Cool', datetime(2019, 3, 8))
        ins(2, 1, 'Lets go for a walk?', datetime(2019, 3, 8))
        ins(2, 3, 'Ok', datetime(2019, 3, 8))
        ins(2, 1, 'See you in half an hour', datetime(2019, 3, 8))
        ins(2, 3, 'Good', datetime(2019, 3, 8))
        ins(2, 1, 'Bye', datetime(2019, 3, 8))

        ins(3, 2, 'Message 1', datetime(2019, 2, 18))
        ins(3, 4, 'Message 2', datetime(2019, 2, 18))
        ins(3, 2, 'Message 3', datetime(2019, 2, 18))
        ins(3, 4, 'Message 4', datetime(2019, 2, 18))
        ins(3, 2, 'Message 5', datetime(2019, 2, 18))
        ins(3, 4, 'Message 6', datetime(2019, 2, 18))
        ins(3, 2, 'Message 7', datetime(2019, 2, 18))
        ins(3, 4, 'Message 8', datetime(2019, 2, 18))
        ins(3, 2, 'Message 9', datetime(2019, 2, 18))
        ins(3, 4, 'Message 10', datetime(2019, 2, 18))

        ins(4, 4, 'Test 1', datetime(2019, 1, 18))
        ins(4, 5, 'Test 2', datetime(2019, 1, 18))
        ins(4, 4, 'Test 3', datetime(2019, 1, 18))
        ins(4, 5, 'Test 4', datetime(2019, 1, 18))
        ins(4, 4, 'Test 5', datetime(2019, 1, 18))
        ins(4, 5, 'Test 6', datetime(2019, 1, 18))
        ins(4, 4, 'Test 7', datetime(2019, 1, 18))
        ins(4, 5, 'Test 8', datetime(2019, 1, 18))
        ins(4, 4, 'Test 9', datetime(2019, 1, 18))
        ins(4, 5, 'Test 10', datetime(2019, 1, 18))

        ins(5, 3, 'A', datetime(2019, 1, 11))
        ins(5, 5, 'B', datetime(2019, 1, 11))
        ins(5, 3, 'C', datetime(2019, 1, 11))
        ins(5, 5, 'D', datetime(2019, 1, 11))
        ins(5, 3, 'E', datetime(2019, 1, 11))
        ins(5, 5, 'F', datetime(2019, 1, 11))
        ins(5, 3, 'G', datetime(2019, 1, 11))
        ins(5, 5, 'H', datetime(2019, 1, 11))
        ins(5, 3, 'I', datetime(2019, 1, 11))
        ins(5, 5, 'J', datetime(2019, 1, 11))


def compare_json_data(source_data_a, source_data_b):
    def compare(data_a, data_b):
        if type(data_a) is list:
            if (
                    (type(data_b) != list) or
                    (len(data_a) != len(data_b))
            ):
                return False
            used_index = []
            for list_index, list_item in enumerate(data_a):
                tmp = 0
                for i in range(len(data_a)):
                    if compare(list_item, data_b[i]) and (not i in used_index):
                        tmp = tmp + 1
                        used_index.append(i)
                        break
                if tmp == 0:
                    return False
            return True
        if type(data_a) is dict:
            if type(data_b) != dict:
                return False
            for dict_key, dict_value in data_a.items():
                if (
                        (dict_key not in data_b) or
                        (not compare(dict_value, data_b[dict_key]))
                ):
                    return False
            return True
        return (
                (data_a == data_b) and
                (type(data_a) is type(data_b))
        )

    return (
            compare(source_data_a, source_data_b) and
            compare(source_data_b, source_data_a)
    )


class JSONRPCTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        generate()
        #create_tables()

    def test_get_messages(self):
        rv = self.app.post('/api/',
                           data=' {"jsonrpc": "2.0", "method": "get_messages", "params": {"limit": 10, "chat_id": 1}, "id": "1"}')
        self.assertEqual(rv.status_code, 200)
        data = {
            'id': '1', 'jsonrpc': '2.0', 'result': {
                '0': [2, 'Chris', 'Cristopher Smith', 9, 'Good morning!', 'Sun, 10 Mar 2019 00:00:00 GMT'],
                '1': [1, 'Tina', 'Margarita Miller', 10, 'Hi!', 'Sun, 10 Mar 2019 00:00:00 GMT'],
                '2': [1, 'Tina', 'Margarita Miller', 6, 'Nothing', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '3': [1, 'Tina', 'Margarita Miller', 4, 'Ok', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '4': [1, 'Tina', 'Margarita Miller', 2, 'How are you?', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '5': [1, 'Tina', 'Margarita Miller', 1, 'Hello!', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '6': [2, 'Chris', 'Cristopher Smith', 7, 'Bye', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '7': [2, 'Chris', 'Cristopher Smith', 5, 'What is the news?', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '8': [2, 'Chris', 'Cristopher Smith', 3, 'Better tnan you', 'Sat, 09 Mar 2019 00:00:00 GMT'],
                '9': [1, 'Tina', 'Margarita Miller', 8, 'Goodbye', 'Sat, 09 Mar 2019 00:00:00 GMT'],
            }
        }
        self.assertTrue(compare_json_data(data, json.loads(rv.data)))

    def test_find_user(self):
        rv = self.app.post('/api/',
                           data='{"jsonrpc": "2.0", "method": "find_user", "params": {"nick": "Tina"}, "id": "2"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '2', 'jsonrpc': '2.0', 'result': {'name': 'Margarita Miller', 'user_id': 1}}
        self.assertTrue(compare_json_data(data, json.loads(rv.data)))

    def test_find_users(self):
        rv = self.app.post('/api/',
                           data='{"jsonrpc": "2.0", "method": "find_users", "params": {"name": "Margarita Miller"}, "id": "3"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '3', 'jsonrpc': '2.0', 'result': {'0': [1, 'Tina']}}
        self.assertTrue(compare_json_data(data, json.loads(rv.data)))

    def test_get_chats_list(self):
        rv = self.app.post('/api/',
                           data='{"jsonrpc": "2.0", "method": "get_chats_list", "params": {"nick": "Al"}, "id": "4"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '4', 'jsonrpc': '2.0', 'result': {'0': [2, 'kvant'], '1': [5, 'home']}}
        self.assertTrue(compare_json_data(data, json.loads(rv.data)))

    # def test_create_personal_chat(self):
    #    rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "create_personal_chat", "params": {"topic": "freedom"}, "id": "5"}')
    #    self.assertEqual(rv.status_code, 200)

    # def test_send_message(self):
    #    rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "send_message", "params": {"nick": "ikate", "chat": "kvant", "content": "hw"}, "id": "6"}')
    #    self.assertEqual(rv.status_code, 200)

    # def test_read_message(self):
    #    rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "read_message", "params": {"nick": "ikate", "chat": "kvant", "content": "hw"}, "id": "7"}')
    #    self.assertEqual(rv.status_code, 200)
