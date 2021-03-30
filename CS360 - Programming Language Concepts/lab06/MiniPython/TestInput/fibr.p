define fib proc( n )
  if 3-n then
    return := 1
  else
    return := fib(n-1) + fib(n-2)
  fi
end;

n := 30;
answer := fib( n )
