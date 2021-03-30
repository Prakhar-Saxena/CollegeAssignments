gcd(U, V, X) :- min(U, V, M), greatestdivisor(U, V, M, X).
greatestdivisor(U, V, M, M) :- divides(U, M), divides(V, M), ! .
greatestdivisor(U, V, M, X) :- N is M - 1 , greatestdivisor(U, V, N, X).
min(U, V, U) :- U < V.
min(U, V, V) :- U >= V.
divides(U, M) :- N is U mod M, N = 0.
