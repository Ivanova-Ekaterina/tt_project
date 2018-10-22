import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'Hello, World', rv.data)
        self.assertEqual("text/html", rv.mimetype)

    def test_login(self):
        rv = self.app.post('/login/', data={"full_name": "Kate", "user_nickname": "Ivanova"})
        self.assertEqual(b'{"full_name":"Kate","user_nickname":"Ivanova"}\n', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_find_user(self):
        rv = self.app.post('/find_user/', data={"full_name": "Kate", "user_nickname": "Ivanova"})
        self.assertEqual(b'{"full_name":"Kate","user_nickname":"Ivanova"}\n', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_find_chat(self):
        rv = self.app.post('/find_chat/', data={"chat_name": "tt", "chat_nickname": "techno"})
        self.assertEqual(b'{"chat_name":"tt","chat_nickname":"techno"}\n', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_get_chats_list(self):
        rv = self.app.get('/get_chats_list/')
        self.assertEqual(b'{"name": ["first", "second"], "nick_name": ["tt", "516"], "participant": [5, 8]}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_create_private_chat(self):
        rv = self.app.post('/create_private_chat/')
        self.assertEqual(b'{"name": "new private chat"}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_create_group_chat(self):
        rv = self.app.post('/create_group_chat/')
        self.assertEqual(b'{"name": "new group chat"}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_add_users_to_chat(self):
        rv = self.app.post('/add_users_to_chat/')
        self.assertEqual(b'{"name": "add user"}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_leave_chat(self):
        rv = self.app.post('/leave_chat/')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'{"name": "leave chat"}', rv.data)
        self.assertEqual("application/json", rv.mimetype)

    def test_send_message(self):
        rv = self.app.post('/send_message/')
        self.assertEqual(b'{"name": "send message"}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_read_message(self):
        rv = self.app.get('/read_message/')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'{"text": "hello", "time": "", "user": "kate"}', rv.data)
        self.assertEqual("application/json", rv.mimetype)

    def test_load_file(self):
        rv = self.app.post('/load_file/')
        self.assertEqual(b'{"name": "new file"}', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)

    def test_get_chats_list_POST(self):
        rv = self.app.post('/get_chats_list/')
        self.assertEqual(405, rv.status_code)

    def test_create_private_chat_GET(self):
        rv = self.app.get('/create_private_chat/')
        self.assertEqual(405, rv.status_code)

    def test_create_group_chat_GET(self):
        rv = self.app.get('/create_group_chat/')
        self.assertEqual(405, rv.status_code)

    def test_add_users_to_chat_GET(self):
        rv = self.app.get('/add_users_to_chat/')
        self.assertEqual(405, rv.status_code)

    def leave_chat_GET(self):
        rv = self.app.get('/leave_chat/')
        self.assertEqual(405, rv.status_code)

    def send_message_GET(self):
        rv = self.app.get('/send_message/')
        self.assertEqual(405, rv.status_code)

    def read_message_POST(self):
        rv = self.app.post('/read_message/')
        self.assertEqual(405, rv.status_code)

    def load_file_GET(self):
        rv = self.app.get('/load_file/')
        self.assertEqual(405, rv.status_code)


if __name__ == "__main__":
    unittest.main()
