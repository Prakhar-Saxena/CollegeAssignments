create table professors (
    pid integer primary key,
    name varchar(50) not null,
    dept varchar(50)
)

create table students (
    sid integer primary key,
    name varchar(50) not null,
    dept varchar(50)
)

create table courses (
    cid integer primary key,
    name varchar(50) not null,
    size integer
)

create table enroll (
    grade varchar(1),
    pid integer,
    sid integer,
    cid integer,
    primary key (pid, sid, cid),
    foreign key (pid) references professors(pid),
    foreign key (sid) references students(sid),
    foreign key (cid) references courses(cid)
)