import qualified Data.List

data (Ord a, Eq a) => Tree a = Nil | Node (Tree a) a (Tree a) 
	deriving Show

member :: (Ord a) => (Tree a) -> a -> Bool
member Nil _ = False
member (Node t1 v t2) x 
	| x == v = True
	| x  < v = member t1 x 
	| x  > v = member t2 x

insert :: (Ord a) => Tree a -> a -> Tree a
insert Nil x = Node Nil x Nil
insert (Node t1 v t2) x 
	| v == x = Node t1 v t2
	| v  < x = Node t1 v (insert t2 x)
	| v  > x = Node (insert t1 x) v t2
