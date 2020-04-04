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

--add course internal link
ALTER TABLE ONLY lectures ADD COLUMN vidcontentlink text;


-- reworking subscription and payments
--tables -> planid, subscriptionid, userid, courseid
--drop column
alter table coursesubscription drop column type;

alter table coursesubscription drop column renewalstatus;

alter table coursesubscription drop column autorenewal;

alter table coursesubscription drop column discount;

alter table coursesubscription drop column discountCode;

--plan
CREATE TABLE plan (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    planid text,
    name text,
    description text,
    fee int,
    courseid int,
    class text,
    addedon text,
    duration int,
    status text
);

CREATE SEQUENCE plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE plan_id_seq OWNED BY plan.id;

ALTER TABLE ONLY plan ALTER COLUMN id SET DEFAULT nextval('plan_id_seq'::regclass);

--add plan to coursesubscription
alter table coursesubscription add column plan integer;

--paymentrequest table
CREATE TABLE paymentrequest (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    requestid text,
    recordedon text,
    pgresponse json,
    amount int,
    discount int,
    discountcode text,
    status text
);

CREATE SEQUENCE paymentrequest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE paymentrequest_id_seq OWNED BY paymentrequest.id;

ALTER TABLE ONLY paymentrequest ALTER COLUMN id SET DEFAULT nextval('paymentrequest_id_seq'::regclass);

--subsciptionpayment table (each subscription mapped to payment)
CREATE TABLE subsciptionpayment (
    "createdAt" character varying,
    "updatedAt" character varying,
    id integer NOT NULL,
    request int NOT NULL,
    subscription int NOT NULL,
    amount int,
    discount int,
    discountcode text,
    status text
);

CREATE SEQUENCE subsciptionpayment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
        
ALTER SEQUENCE subsciptionpayment_id_seq OWNED BY subsciptionpayment.id;

ALTER TABLE ONLY subsciptionpayment ALTER COLUMN id SET DEFAULT nextval('subsciptionpayment_id_seq'::regclass);

--plans -> add discountpercent, basemultiplier, totalfee drop fee?
alter table plan drop column fee;

alter table plan add column discountpercent int;

alter table plan add column basemultiplier numeric;

--paymentrequest add user, 
alter table paymentrequest add column user int;
