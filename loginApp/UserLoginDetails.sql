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

--courses
CREATE TABLE courses (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    courseid text,
    title text,
    description text,
    subject text,
    designedfor text,
    courseof int,
    subscriptionfee int,
    numlectures int,
    startdate character varying,
    numsubscribers int,
    lastupdated character varying,
    status text
);

CREATE SEQUENCE courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE courses_id_seq OWNED BY courses.id;

ALTER TABLE ONLY courses ALTER COLUMN id SET DEFAULT nextval('courses_id_seq'::regclass);

--lectures
CREATE TABLE lectures (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    lectureid text,
    courseid int,
    lectureof int,
    type text,
    topic text,
    description text,
    startdateandtime character varying,
    duration int,
    validitystatus text,
    status text
);

CREATE SEQUENCE lectures_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE lectures_id_seq OWNED BY lectures.id;

ALTER TABLE ONLY lectures ALTER COLUMN id SET DEFAULT nextval('lectures_id_seq'::regclass);

--course subscription
CREATE TABLE coursesubscription (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    subscriptionid text,
    userid integer,
    courseid int,
    courseof int,
    type text,
    subscribedon text,
    renewalstatus text,
    autorenewal text,
    feepaid int,
    discount int,
    discountCode text,
    status text
);

CREATE SEQUENCE coursesubscription_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE coursesubscription_id_seq OWNED BY coursesubscription.id;

ALTER TABLE ONLY coursesubscription ALTER COLUMN id SET DEFAULT nextval('coursesubscription_id_seq'::regclass);

--subscriptiontype



