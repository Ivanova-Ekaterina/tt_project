from unittest import TestCase
from unittest.mock import patch, Mock
from app import app


class TestCreateChat(TestCase):
    @patch('app.create_personal_chat')
    def test_create_chat(self, Mock):
        mock = Mock()
        mock.create_personal_chat.return_value = {
            "topic": "test",
            "chat_id": 1,
            "is_group_chat": False
        }
        response = mock.create_personal_chat('test')
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

        self.assertEqual(response['topic'], "test")
        self.assertEqual(response['chat_id'], 1)
        self.assertFalse(response['is_group_chat'])