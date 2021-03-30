
--Node comprises of Char for symbols and Int for weights
-- [Char] for combined nodes
--Show to display a node
data Node = Leaf Char Int | NonLeaf Node Node [Char] Int deriving (Show)




--This is recursive so I need the extra input for tree
encode :: Node -> Node -> [Char] -> [Int]

--If the symbol is nothing we are done
encode _ _ [] = []
--Else 
encode tree (Leaf symbol weight) (firstSymbol:symbols) = encode tree tree symbols
encode tree (NonLeaf leftChild rightChild _ _) (firstSymbol : symbols) | 
	elem firstSymbol (getSymbol leftChild) = 0 : encode tree leftChild (firstSymbol:symbols)| otherwise = 1  : encode tree rightChild (firstSymbol:symbols)
	
	
	
--This is recursive so I need the extra input for tree
decode :: Node -> Node -> [Int] -> [Char]

--Traverse the tree while keeping track of the path
decode tree (Leaf symbol w) hCode = symbol : decode tree tree hCode

--Once the code is finished we are complete
decode _ _ [] = []
--Otherwise traverse left or right 
decode tree (NonLeaf leftChild _ _ _) (0:hCode) = decode tree leftChild hCode
decode tree (NonLeaf _ rightChild _ _) (1:hCode) = decode tree rightChild hCode



--Create a tree from a list of nodes, since nodes can be either this will work with either leaf or nonleaf	
constructTree :: [Node] -> Node

--A single node is a tree
constructTree [n] = n
constructTree (leftChild:rightChild:tree) = 
--Input must be ordered by weight, this will loop through and create the tree based on input. Combining weights, etc
--Call it recursively
    let node = NonLeaf leftChild rightChild (  (getSymbol leftChild) ++ (getSymbol rightChild)  ) (  (getWeight leftChild) + (getWeight rightChild)  ) in constructTree(insertNode node tree)


--HELPER Functions
	
-- This will just return the symbol from a node
getSymbol :: Node -> [Char]

getSymbol (Leaf symbol _) = [symbol]
getSymbol (NonLeaf _ _ symbol _) = symbol


--Return the weight of a node
getWeight :: Node -> Int

getWeight (Leaf _ weight) = weight
getWeight (NonLeaf _ _ _ weight) = weight



--Function to insert a node into another, for bulding the tree
insertNode :: Node -> [Node] -> [Node]

insertNode node [] = [node]
--Traverse until the weight of the node to be inserted is less than the current node
insertNode node (leftChild:tree) | getWeight node <= getWeight leftChild = node : (leftChild:tree) | otherwise = leftChild : (insertNode node tree)
			
