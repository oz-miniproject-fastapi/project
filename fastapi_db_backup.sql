--
-- PostgreSQL database dump
--

\restrict wlOTwRqYfDZiwaABuAoNSghcKfrfVrLqKLKWBPErkVBbGI8gUctnLAgMNGUHkM1

-- Dumped from database version 14.19 (Homebrew)
-- Dumped by pg_dump version 14.19 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: aerich; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.aerich (
    id integer NOT NULL,
    version character varying(255) NOT NULL,
    app character varying(100) NOT NULL,
    content jsonb NOT NULL
);


ALTER TABLE public.aerich OWNER TO admin1;

--
-- Name: aerich_id_seq; Type: SEQUENCE; Schema: public; Owner: admin1
--

CREATE SEQUENCE public.aerich_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aerich_id_seq OWNER TO admin1;

--
-- Name: aerich_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin1
--

ALTER SEQUENCE public.aerich_id_seq OWNED BY public.aerich.id;


--
-- Name: diary; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.diary (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    content text NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.diary OWNER TO admin1;

--
-- Name: diary_emotion; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.diary_emotion (
    diary_id integer NOT NULL,
    emotionkeyword_id integer NOT NULL
);


ALTER TABLE public.diary_emotion OWNER TO admin1;

--
-- Name: diary_id_seq; Type: SEQUENCE; Schema: public; Owner: admin1
--

CREATE SEQUENCE public.diary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.diary_id_seq OWNER TO admin1;

--
-- Name: diary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin1
--

ALTER SEQUENCE public.diary_id_seq OWNED BY public.diary.id;


--
-- Name: diary_tag; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.diary_tag (
    diary_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.diary_tag OWNER TO admin1;

--
-- Name: emotionkeyword; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.emotionkeyword (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.emotionkeyword OWNER TO admin1;

--
-- Name: emotionkeyword_id_seq; Type: SEQUENCE; Schema: public; Owner: admin1
--

CREATE SEQUENCE public.emotionkeyword_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emotionkeyword_id_seq OWNER TO admin1;

--
-- Name: emotionkeyword_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin1
--

ALTER SEQUENCE public.emotionkeyword_id_seq OWNED BY public.emotionkeyword.id;


--
-- Name: tag; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.tag OWNER TO admin1;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: admin1
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO admin1;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin1
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: admin1
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    nickname character varying(50),
    name character varying(50),
    phone character varying(20),
    is_verified boolean DEFAULT false NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public."user" OWNER TO admin1;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin1
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO admin1;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin1
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: aerich id; Type: DEFAULT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.aerich ALTER COLUMN id SET DEFAULT nextval('public.aerich_id_seq'::regclass);


--
-- Name: diary id; Type: DEFAULT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary ALTER COLUMN id SET DEFAULT nextval('public.diary_id_seq'::regclass);


--
-- Name: emotionkeyword id; Type: DEFAULT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.emotionkeyword ALTER COLUMN id SET DEFAULT nextval('public.emotionkeyword_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: aerich; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.aerich (id, version, app, content) FROM stdin;
\.


--
-- Data for Name: diary; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.diary (id, title, content, created_at, updated_at, user_id) FROM stdin;
1	string	string	2025-09-02 01:50:43.707615-07	2025-09-02 01:50:43.707622-07	1
2	string	string	2025-09-02 01:52:47.98819-07	2025-09-02 01:52:47.988197-07	1
3	string	string	2025-09-02 01:54:03.601225-07	2025-09-02 01:54:03.601242-07	1
4	string	string	2025-09-02 10:19:08.022716-07	2025-09-02 10:19:08.022725-07	9
7	행복한 하루	오랜만에 가족과 함께 맛있는 저녁을 먹고 산책했다. 마음이 평온했다.	2025-09-02 18:37:31.984214-07	2025-09-02 18:37:31.984226-07	12
8	오늘 하루는 즐거웠어요	아침에 산책을 하고, 친구들과 점심을 먹으며 즐거운 시간을 보냈습니다. 날씨도 맑아서 기분이 좋았습니다.	2025-09-02 18:56:37.208696-07	2025-09-02 18:56:37.208712-07	13
9	행복한 하루	오늘 하루는 정말 행복했습니다! 친구들과 즐거운 시간을 보냈어요.	2025-09-02 19:06:23.343023-07	2025-09-02 19:06:23.343042-07	13
10	행복한 하루	오늘 하루는 정말 행복했습니다! 친구들과 즐거운 시간을 보냈어요.	2025-09-02 19:21:21.065652-07	2025-09-02 19:21:21.065659-07	14
11	테스트일기	오늘은 새로운 기능을 테스트하면서 다이어리를 작성해보았다.	2025-09-02 20:30:07.507217-07	2025-09-02 20:30:07.507231-07	15
12	테스트 일기	오늘은 FastAPI 배포 테스트를 위해 일기를 작성했습니다. 서버와 DB 연결 상태를 확인했습니다.	2025-09-02 20:40:16.533205-07	2025-09-02 20:40:16.533218-07	4
\.


--
-- Data for Name: diary_emotion; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.diary_emotion (diary_id, emotionkeyword_id) FROM stdin;
\.


--
-- Data for Name: diary_tag; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.diary_tag (diary_id, tag_id) FROM stdin;
7	2
7	3
7	4
8	3
8	5
8	6
9	3
9	6
9	7
10	3
10	6
10	7
11	8
11	9
11	10
12	8
12	11
12	12
\.


--
-- Data for Name: emotionkeyword; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.emotionkeyword (id, name) FROM stdin;
\.


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public.tag (id, name) FROM stdin;
1	string
2	가족
3	행복
4	산책
5	일상
6	친구
7	즐거움
8	테스트
9	다이어리
10	개발
11	배포
12	FastAPI
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: admin1
--

COPY public."user" (id, email, password, nickname, name, phone, is_verified, created_at) FROM stdin;
1	user13@example.com	$2b$12$WL1S7FxKB9CesmG28tVtfe1bCSLT4am8K6DoAwZOon/vPESsZotTS	string	\N	string	f	2025-09-02 01:27:54.671145-07
2	user@111example.com	$2b$12$aaGnC84kxftFZy8jqUnvD.Aheetjg1sd/l7IfQ4XgL887OjKNvNxq	string	\N	string	f	2025-09-02 09:20:49.782399-07
3	user@222example.com	$2b$12$uSvHYUav3HJP7yoZk9JqLO1h9BeGUKW7krL2rp2QEeJ34tgCIEb22	string	\N	string	f	2025-09-02 09:25:24.276302-07
4	user3333@example.com	$2b$12$x5UPp3Vrucr2lXAmDI/ODOYyEi9QY8G3kx8VLJtpnuT220JJW4xni	string	\N	string	f	2025-09-02 09:40:20.358983-07
5	user11111@example.com	$2b$12$NGCdLo5QUP1cR0y90Ly3nuI827REakq7GSiaSXezb4MFjnudgwjDq	string	\N	string	f	2025-09-02 09:47:26.906327-07
6	user88@example.com	$2b$12$devj/PibkPW9tcXzGOoll.JvsvzQv/bTQKVMKay6tWSNQqTUyKGHK	string	\N	string	f	2025-09-02 10:04:30.362553-07
9	users@example.com	$2b$12$L5U/Dn1chlbtxDX9IuJ2AuGInhLQlUYq45Ax9tuRU7DCGcmra8FBS	string	\N	string	f	2025-09-02 10:17:46.101317-07
11	user333@example.com	$2b$12$lMjksRz6ri4l4/qHv/UtD.zxS.2TH2Z.t/QI2h6amY8BsvIq9yEp6	strin2g	string	string	f	2025-09-02 11:15:20.548198-07
12	user22222@example.com	$2b$12$IOvqiro2sX906eWNlb3tqeKJwMqIYXiAnJkhsQZ8jWGlh2//AuM3e	string	\N	string	f	2025-09-02 18:36:28.47081-07
13	kkkk@example.com	$2b$12$MhUlJwFsFxEvJLJsIQVMrOndulYXxq3ayO1v/ikfki0trjRvT/Pa6	string	\N	string	f	2025-09-02 18:55:44.757419-07
14	user1234@example.com	$2b$12$H0y3STvmG5VKNU9uDvhGJewtiBJkRDweMrsFyjnkvQagPgWsyQQ9a	string	\N	string	f	2025-09-02 19:20:33.275347-07
15	user123456@example.com	$2b$12$lP5WA8xTaVov0/F6nEOTheAagrlScAiSKqugxjGRwNqdR99JG/Vna	string	\N	string	f	2025-09-02 20:29:13.612479-07
\.


--
-- Name: aerich_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin1
--

SELECT pg_catalog.setval('public.aerich_id_seq', 1, false);


--
-- Name: diary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin1
--

SELECT pg_catalog.setval('public.diary_id_seq', 12, true);


--
-- Name: emotionkeyword_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin1
--

SELECT pg_catalog.setval('public.emotionkeyword_id_seq', 1, false);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin1
--

SELECT pg_catalog.setval('public.tag_id_seq', 12, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin1
--

SELECT pg_catalog.setval('public.user_id_seq', 15, true);


--
-- Name: aerich aerich_pkey; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.aerich
    ADD CONSTRAINT aerich_pkey PRIMARY KEY (id);


--
-- Name: diary diary_pkey; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary
    ADD CONSTRAINT diary_pkey PRIMARY KEY (id);


--
-- Name: emotionkeyword emotionkeyword_name_key; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.emotionkeyword
    ADD CONSTRAINT emotionkeyword_name_key UNIQUE (name);


--
-- Name: emotionkeyword emotionkeyword_pkey; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.emotionkeyword
    ADD CONSTRAINT emotionkeyword_pkey PRIMARY KEY (id);


--
-- Name: tag tag_name_key; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_name_key UNIQUE (name);


--
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: uidx_diary_emoti_diary_i_b3b945; Type: INDEX; Schema: public; Owner: admin1
--

CREATE UNIQUE INDEX uidx_diary_emoti_diary_i_b3b945 ON public.diary_emotion USING btree (diary_id, emotionkeyword_id);


--
-- Name: uidx_diary_tag_diary_i_47c64b; Type: INDEX; Schema: public; Owner: admin1
--

CREATE UNIQUE INDEX uidx_diary_tag_diary_i_47c64b ON public.diary_tag USING btree (diary_id, tag_id);


--
-- Name: diary_emotion diary_emotion_diary_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary_emotion
    ADD CONSTRAINT diary_emotion_diary_id_fkey FOREIGN KEY (diary_id) REFERENCES public.diary(id) ON DELETE CASCADE;


--
-- Name: diary_emotion diary_emotion_emotionkeyword_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary_emotion
    ADD CONSTRAINT diary_emotion_emotionkeyword_id_fkey FOREIGN KEY (emotionkeyword_id) REFERENCES public.emotionkeyword(id) ON DELETE CASCADE;


--
-- Name: diary_tag diary_tag_diary_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary_tag
    ADD CONSTRAINT diary_tag_diary_id_fkey FOREIGN KEY (diary_id) REFERENCES public.diary(id) ON DELETE CASCADE;


--
-- Name: diary_tag diary_tag_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary_tag
    ADD CONSTRAINT diary_tag_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tag(id) ON DELETE CASCADE;


--
-- Name: diary diary_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin1
--

ALTER TABLE ONLY public.diary
    ADD CONSTRAINT diary_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: admin
--

GRANT ALL ON SCHEMA public TO admin1;


--
-- PostgreSQL database dump complete
--

\unrestrict wlOTwRqYfDZiwaABuAoNSghcKfrfVrLqKLKWBPErkVBbGI8gUctnLAgMNGUHkM1

