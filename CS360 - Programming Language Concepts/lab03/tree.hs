{- Implementation of BST (binary search tree)
 - Script is absolutly free/libre, but with no guarantee.
 - Author: Ondrej Profant -}

import qualified Data.List

{- DEF data structure -}
data (Ord a, Eq a) => Tree a = Nil | Node (Tree a) a (Tree a) 
	deriving Show

{- BASIC Information -}
empty :: (Ord a) => Tree a -> Bool
empty Nil = True
empty  _  = False

contains :: (Ord a) => (Tree a) -> a -> Bool
contains Nil _ = False
contains (Node t1 v t2) x 
	| x == v = True
	| x  < v = contains t1 x 
	| x  > v = contains t2 x

{- BASIC Manipulation -}
insert :: (Ord a) => Tree a -> a -> Tree a
insert Nil x = Node Nil x Nil
insert (Node t1 v t2) x 
	| v == x = Node t1 v t2
	| v  < x = Node t1 v (insert t2 x)
	| v  > x = Node (insert t1 x) v t2

