--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)
-- Dumped by pg_dump version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: attachments; Type: TABLE; Schema: public; Owner: chat
--

CREATE TABLE public.attachments (
    attach_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    message_id integer NOT NULL,
    type text NOT NULL,
    url text NOT NULL,
    CONSTRAINT attachments_type_check CHECK ((length(type) < 256)),
    CONSTRAINT attachments_url_check CHECK ((length(url) < 65536))
);


ALTER TABLE public.attachments OWNER TO chat;

--
-- Name: attachments_attach_id_seq; Type: SEQUENCE; Schema: public; Owner: chat
--

CREATE SEQUENCE public.attachments_attach_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attachments_attach_id_seq OWNER TO chat;

--
-- Name: attachments_attach_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chat
--

ALTER SEQUENCE public.attachments_attach_id_seq OWNED BY public.attachments.attach_id;


--
-- Name: chats; Type: TABLE; Schema: public; Owner: chat
--

CREATE TABLE public.chats (
    chat_id integer NOT NULL,
    is_group_chat boolean,
    topic text NOT NULL,
    last_message text NOT NULL,
    CONSTRAINT chats_last_message_check CHECK ((length(last_message) < 65536)),
    CONSTRAINT chats_topic_check CHECK ((length(topic) < 256))
);


ALTER TABLE public.chats OWNER TO chat;

--
-- Name: chats_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: chat
--

CREATE SEQUENCE public.chats_chat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chats_chat_id_seq OWNER TO chat;

--
-- Name: chats_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chat
--

ALTER SEQUENCE public.chats_chat_id_seq OWNED BY public.chats.chat_id;


--
-- Name: members; Type: TABLE; Schema: public; Owner: chat
--

CREATE TABLE public.members (
    member_id integer NOT NULL,
    user_id integer NOT NULL,
    chat_id integer NOT NULL,
    new_messages text NOT NULL,
    last_read_message_id integer,
    CONSTRAINT members_new_messages_check CHECK ((length(new_messages) < 65536))
);


ALTER TABLE public.members OWNER TO chat;

--
-- Name: members_member_id_seq; Type: SEQUENCE; Schema: public; Owner: chat
--

CREATE SEQUENCE public.members_member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.members_member_id_seq OWNER TO chat;

--
-- Name: members_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chat
--

ALTER SEQUENCE public.members_member_id_seq OWNED BY public.members.member_id;


--
-- Name: messages; Type: TABLE; Schema: public; Owner: chat
--

CREATE TABLE public.messages (
    message_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    content text NOT NULL,
    added_at timestamp without time zone DEFAULT now() NOT NULL,
    CONSTRAINT messages_content_check CHECK ((length(content) < 65536))
);


ALTER TABLE public.messages OWNER TO chat;

--
-- Name: messages_message_id_seq; Type: SEQUENCE; Schema: public; Owner: chat
--

CREATE SEQUENCE public.messages_message_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messages_message_id_seq OWNER TO chat;

--
-- Name: messages_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chat
--

ALTER SEQUENCE public.messages_message_id_seq OWNED BY public.messages.message_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: chat
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name text NOT NULL,
    nick text NOT NULL,
    CONSTRAINT users_name_check CHECK ((length(name) < 32)),
    CONSTRAINT users_nick_check CHECK ((length(nick) < 32))
);


ALTER TABLE public.users OWNER TO chat;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: chat
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO chat;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chat
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: attachments attach_id; Type: DEFAULT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.attachments ALTER COLUMN attach_id SET DEFAULT nextval('public.attachments_attach_id_seq'::regclass);


--
-- Name: chats chat_id; Type: DEFAULT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.chats ALTER COLUMN chat_id SET DEFAULT nextval('public.chats_chat_id_seq'::regclass);


--
-- Name: members member_id; Type: DEFAULT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.members ALTER COLUMN member_id SET DEFAULT nextval('public.members_member_id_seq'::regclass);


--
-- Name: messages message_id; Type: DEFAULT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.messages ALTER COLUMN message_id SET DEFAULT nextval('public.messages_message_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: attachments; Type: TABLE DATA; Schema: public; Owner: chat
--

COPY public.attachments (attach_id, chat_id, user_id, message_id, type, url) FROM stdin;
\.


--
-- Data for Name: chats; Type: TABLE DATA; Schema: public; Owner: chat
--

COPY public.chats (chat_id, is_group_chat, topic, last_message) FROM stdin;
\.


--
-- Data for Name: members; Type: TABLE DATA; Schema: public; Owner: chat
--

COPY public.members (member_id, user_id, chat_id, new_messages, last_read_message_id) FROM stdin;
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: chat
--

COPY public.messages (message_id, chat_id, user_id, content, added_at) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: chat
--

COPY public.users (user_id, name, nick) FROM stdin;
\.


--
-- Name: attachments_attach_id_seq; Type: SEQUENCE SET; Schema: public; Owner: chat
--

SELECT pg_catalog.setval('public.attachments_attach_id_seq', 1, false);


--
-- Name: chats_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: chat
--

SELECT pg_catalog.setval('public.chats_chat_id_seq', 1, false);


--
-- Name: members_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: chat
--

SELECT pg_catalog.setval('public.members_member_id_seq', 1, false);


--
-- Name: messages_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: chat
--

SELECT pg_catalog.setval('public.messages_message_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: chat
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- Name: attachments attachments_pkey; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.attachments
    ADD CONSTRAINT attachments_pkey PRIMARY KEY (attach_id);


--
-- Name: chats chats_pkey; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.chats
    ADD CONSTRAINT chats_pkey PRIMARY KEY (chat_id);


--
-- Name: members members_pkey; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (member_id);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (message_id);


--
-- Name: users users_nick_key; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_nick_key UNIQUE (nick);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: attachments attachments_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.attachments
    ADD CONSTRAINT attachments_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chats(chat_id);


--
-- Name: attachments attachments_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.attachments
    ADD CONSTRAINT attachments_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.messages(message_id);


--
-- Name: attachments attachments_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.attachments
    ADD CONSTRAINT attachments_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: members members_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chats(chat_id);


--
-- Name: members members_last_read_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_last_read_message_id_fkey FOREIGN KEY (last_read_message_id) REFERENCES public.messages(message_id);


--
-- Name: members members_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: messages messages_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chats(chat_id);


--
-- Name: messages messages_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: chat
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

