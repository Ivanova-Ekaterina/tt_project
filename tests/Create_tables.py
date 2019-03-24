import psycopg2
from app import app

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
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
        """)



    conn = None
    try:
        # read the connection parameters
        params = app.config.TestingConfig()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
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

