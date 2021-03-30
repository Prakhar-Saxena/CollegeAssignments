-- This is for Q1

select cid,name
from courses


-- This is for Q2

select *
from students
where dept = "cs"


-- This is for Q3

select s.name
from professors as p, students as s, courses as c, enroll as e
where e.pid = p.pid
and e.sid = s.sid
and e.cid = c.cid
and p.name = "alberto mendelzon"


-- This is for Q4

select s.name, e.grade
from professors as p, students as s, courses as c, enroll as e
where e.pid = p.pid
and e.sid = s.sid
and e.cid = 461