-- user profile table
CREATE TABLE userprofile (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    userid text,
    email text,
    phone text,
    firstname text,
    lastname text,
    password text,
    refid text
);

CREATE SEQUENCE userprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE userprofile_id_seq OWNED BY userprofile.id;

ALTER TABLE ONLY userprofile ALTER COLUMN id SET DEFAULT nextval('userprofile_id_seq'::regclass);

ALTER TABLE ONLY userprofile ADD COLUMN isteacher text;

