define sum 
proc(n)
  i := n;
  s := 0;
  while i do s := s + i;  i := i-1 od;
  return := s
end;

x := 7;
if x then
  s := sum(x)
else
  x := 0 - x
fi

