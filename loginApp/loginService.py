create database dharna2;
create user db_user identified by 'mohit';


CREATE TABLE user (
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
