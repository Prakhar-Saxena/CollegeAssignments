insert into students (sid, name, dept)
values (1, "Prakhar Saxena", "Computer Science")

insert into students (sid, name, dept)
values (2, "Paul McCartney", "Music")

insert into students (sid, name, dept)
values (3, "John Lennon", "Music")


insert into professors (pid, name, dept)
values (1, "Dimitra Vista", "Computer Science")

insert into professors (pid, name, dept)
values (2, "Pink Floyd", "Music")

insert into courses (cid, name, size)
values (1, "Database Systems", 2)

insert into courses (cid, name, size)
values (2, "Music", 2)

insert into enroll (grade, pid, sid, cid)
values ("A", 1, 1, 1)

insert into enroll (grade, pid, sid, cid)
values ("A", 2, 2, 2)

insert into enroll (grade, pid, sid, cid)
values ("B", 2, 3, 2)