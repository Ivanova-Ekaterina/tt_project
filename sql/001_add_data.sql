insert into Users (nick, name)
values ('ikate', 'ivanova ekaterina'),
	   ('ester', 'ivanova tatiana'),
	   ('free', 'chernonog viacheslav'),
	   ('blocher', 'matveeva sveta');

insert into Chats (is_group_chat, topic, last_message)
values (false, 'tt', 'create chat'),
	   (false, 'kvant', 'create chat');

insert into Messages (chat_id, user_id, content, added_at)
values (1, 1, 'Hello!', '1997-11-29'),
	   (1, 4, 'How are you?', '1998-09-14'),
	   (2, 3, 'Better tnan you', '1997-05-14');

insert into members (chat_id, user_id, new_messages)
values (1, 1, 'hi'),
	   (1, 4, 'hi'),
	   (2, 1, 'hi'),
	   (2, 3, 'hi');