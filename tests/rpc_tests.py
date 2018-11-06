from unittest import TestCase
from app import app
import json


def compare_json_data(source_data_a,source_data_b):
    def compare(data_a,data_b):
        if (type(data_a) is list):
            if (
                (type(data_b) != list) or
                (len(data_a) != len(data_b))
            ):
                return False
            for list_index,list_item in enumerate(data_a):
                if (not compare(list_item,data_b[list_index])):
                    return False
            return True
        if (type(data_a) is dict):
            if (type(data_b) != dict):
                 return False
            for dict_key,dict_value in data_a.items():
                 if (
                     (dict_key not in data_b) or
                     (not compare(dict_value,data_b[dict_key]))
                 ):
                      return False
            return True
        return (
            (data_a == data_b) and
            (type(data_a) is type(data_b))
		)
    return (
        compare(source_data_a,source_data_b) and
        compare(source_data_b,source_data_a)
	)

class JSONRPCTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_messages(self):
        rv = self.app.post('/api/', data=' {"jsonrpc": "2.0", "method": "get_messages", "params": {"limit": 10, "chat_id": 1}, "id": "1"}')
        self.assertEqual(rv.status_code, 200)
        data = {
                'id': '1', 'jsonrpc': '2.0', 'result': {
                    '0': [1, 'ikate', 'ivanova ekaterina', 1, 'Hello!', 'Tue, 30 Oct 2018 18:22:11 GMT'], 
                    '1': [4, 'blocher', 'matveeva sveta', 2, 'How are you?', 'Tue, 30 Oct 2018 18:22:11 GMT']
                    }
               }
        self.assertEqual(True, compare_json_data(data, json.loads(rv.data)))

    def test_find_user(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "find_user", "params": {"nick": "ikate"}, "id": "2"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '2', 'jsonrpc': '2.0', 'result': {'name': 'ivanova ekaterina', 'user_id': 1}}
        self.assertEqual(True, compare_json_data(data, json.loads(rv.data)))

    def test_find_users(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "find_users", "params": {"name": "ivanova ekaterina"}, "id": "3"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '3', 'jsonrpc': '2.0', 'result': {'0': [1, 'ikate']}}
        self.assertEqual(True, compare_json_data(data, json.loads(rv.data)))

    def test_get_chats_list(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "get_chats_list", "params": {"nick": "ikate"}, "id": "4"}')
        self.assertEqual(rv.status_code, 200)
        data = {'id': '4', 'jsonrpc': '2.0', 'result': {'0': [1, 'tt'], '1': [2, 'kvant']}}
        self.assertEqual(True, compare_json_data(data, json.loads(rv.data)))

    def test_create_personal_chat(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "create_personal_chat", "params": {"topic": "freedom"}, "id": "5"}')
        self.assertEqual(rv.status_code, 200)

    def test_send_message(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "send_message", "params": {"nick": "ikate", "chat": "kvant", "content": "hw"}, "id": "6"}')
        self.assertEqual(rv.status_code, 200)

    def test_read_message(self):
        rv = self.app.post('/api/', data='{"jsonrpc": "2.0", "method": "read_message", "params": {"nick": "ikate", "chat": "kvant", "content": "hw"}, "id": "7"}')
        self.assertEqual(rv.status_code, 200)


