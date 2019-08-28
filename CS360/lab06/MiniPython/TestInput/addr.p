define addr 
proc(i)
  if i then
    return := i + addr(i-1)
  else
    return := 0
  fi
end;

n := 7;
s := addr( n )

