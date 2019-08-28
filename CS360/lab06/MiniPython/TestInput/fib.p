define fib proc( n )
  a := 1;
  b := 1;
  i := 3;
  while n-i+1 do
    t := a + b;
    b := a;
    a := t;
    i := i+1
  od;
  return := a
end;

n := 30;
answer := fib( n )
