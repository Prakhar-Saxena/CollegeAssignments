define sum
proc(mylist)
    current := mylist;
    total := 0;
    while (null current) == 0 do
        total := total + (car current);
        current := cdr current
    od;
    return := total
end;

a := [1, 2, 3, 4, 3+2, 7, 4*2];
b := car a ;
c := cdr a ;
d := cons 10, a ;
e := null [];
f := null a;
g := sum(a)