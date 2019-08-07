-- A Pythagorean Triple is a tuple of integers (x,y,z)
-- such that x^2 + y^2 = z^2
-- The function pyth n prints out all pythagorean triples
-- such that 1 <= x <= y <= z <= n

pyth n = [(x,y,z) | x <- [1..n], y <- [x..n], z <- [y..n], z^2==x^2+y^2]