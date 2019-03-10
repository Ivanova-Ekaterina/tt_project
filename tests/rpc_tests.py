from unittest import TestCase
from app import app
import json
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
