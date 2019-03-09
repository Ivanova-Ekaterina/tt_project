CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name text NOT NULL,
    nick text NOT NULL,
    avatar text
);
CREATE TABLE chats (
    chat_id SERIAL PRIMARY KEY,
    is_group_chat boolean,
    topic text NOT NULL,
    last_message text NOT NULL
);
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    chat_id INTEGER REFERENCES chats(chat_id),
    user_id INTEGER REFERENCES users(user_id),
    content text NOT NULL,
    added_at timestamp NOT NULL
);
CREATE TABLE attachments (
    attach_id SERIAL PRIMARY KEY,
	message_id INTEGER REFERENCES messages(message_id),
	chat_id INTEGER REFERENCES chats(chat_id),
	user_id INTEGER REFERENCES users(user_id),
    type text NOT NULL,
    url text NOT NULL
);
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
	chat_id INTEGER REFERENCES chats(chat_id),
	user_id INTEGER REFERENCES users(user_id),
    new_messages text NOT NULL,
	last_read_message_id INTEGER REFERENCES messages(message_id)
);
