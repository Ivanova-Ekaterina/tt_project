import postgresql
from datetime import datetime
import Create_tables

def generate():
    Create_tables.create_tables()
    with postgresql.open('pq://ekaterina:@localhost/track_test') as db:

        db.drop_all()

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

        ins(1, 1, 'Hello!',  datetime(2019, 3, 9))
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