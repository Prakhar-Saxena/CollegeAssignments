--The Sieve of Eratosthenes
-- Takes an infinite list of positive integers starting at 2
-- Filters out all numbers that are not prime
-- first filter out numbers divisible by 2, then divisible by 3, etc
sieve (p:lis) = p : sieve [n | n <- lis, mod n p /= 0]

--Create an infinite list of primes
primes = sieve [2..]

--A Twin Prime is a set of two primes where both p and p+2 or p and p-2 are prime
--The list of primes is ordered, so it is easy to search.
--We always know if we went to far
orderedSearch a (h:t) = if a < h then False else (if a == h then True else orderedSearch a t )

-- We want to filter the list of primes to only contain twin primes
-- Assuming a is a prime, check if a+2 or a-2 is also prime
isTwinPrime a = (orderedSearch (a+2) primes) || (orderedSearch (a-2) primes)

--Filter the infinite list of primes into a list of twin primes
tprimes = filter isTwinPrime primes
