define sum 
proc(n)
  i := 0;
  s := 0;
  while i < n do s := s + i;  i := i+1 od;
  return := s
end;

x := 7;
if x then
  s := sum(x)
else
  x := 0 - x
fi

