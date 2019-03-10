import unittest
from app import app
import json
from test import CompareJSON

class AppTest(unittest.TestCase):
    def setUp(self):
       self.app = app.test_client()

    def test_messages(self):
        rv = self.app.get('/messages/?limit=5&chat_id=1')
        self.assertEqual(200, rv.status_code)
        data = {
                  "1": [
                         4,
                         "blocher",
                         "matveeva sveta",
                         2,
                         "How are you?",
                         "Tue, 30 Oct 2018 18:22:11 GMT"
                       ],
                  "0": [
                         1,
                         "ikate",
                         "ivanova ekaterina",
                         1,
                         "Hello!",
                         "Tue, 30 Oct 2018 18:22:11 GMT"
                       ]
                }
        self.assertEqual(True, CompareJSON.compare_json_data(data, json.loads(rv.data)))
        self.assertEqual("application/json", rv.mimetype)

    def test_find_user(self):
        rv = self.app.get('/find_user/?nick=ikate')
        self.assertEqual(200, rv.status_code)
        data = {
                 "name": "ivanova ekaterina",
                 "user_id": 1
               }
        self.assertEqual(True, CompareJSON.compare_json_data(data, json.loads(rv.data)))
        self.assertEqual("application/json", rv.mimetype)

    def test_find_users(self):
        rv = self.app.get('/find_users/?name=ivanova ekaterina')
        self.assertEqual(200, rv.status_code)
        data = {
                "0": [
                        1,
                        "ikate"
                     ]
               }
        self.assertEqual(True, CompareJSON.compare_json_data(data, json.loads(rv.data)))
        self.assertEqual("application/json", rv.mimetype)

    def test_get_chat_lists(self):
        rv = self.app.get('/get_chats_list/?nick=ikate')
        self.assertEqual(200, rv.status_code)
        data = {
                "0": [
                         1,
                         "tt"
                     ],
                "1": [
                         2,
                         "kvant"
                     ]
               }
        self.assertEqual(True, CompareJSON.compare_json_data(data, json.loads(rv.data)))
        self.assertEqual("application/json", rv.mimetype)

    def test_create_personal_chat(self):
        rv = self.app.post('/create_personal_chat/')
        self.assertEqual(204, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)


