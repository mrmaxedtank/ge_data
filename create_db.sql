-- TODO:
-- carefully review configuration.
-- fix key generation for records ("serial")
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

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
-- Name: items; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.items (
    key integer NOT NULL,
    item_id character varying(30) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.items OWNER TO pi;

--
-- Name: items_key_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.items_key_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_key_seq OWNER TO pi;

--
-- Name: items_key_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.items_key_seq OWNED BY public.items.key;


--
-- Name: records; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.records (
    id integer NOT NULL,
    record_datetime timestamp without time zone NOT NULL,
    item_id character varying(30),
    price integer NOT NULL,
    source character varying(20)
);


ALTER TABLE public.records OWNER TO pi;

--
-- Name: records_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.records_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.records_id_seq OWNER TO pi;

--
-- Name: records_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.records_id_seq OWNED BY public.records.id;


--
-- Name: items key; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.items ALTER COLUMN key SET DEFAULT nextval('public.items_key_seq'::regclass);


--
-- Name: records id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.records ALTER COLUMN id SET DEFAULT nextval('public.records_id_seq'::regclass);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (key);


--
-- Name: records records_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

