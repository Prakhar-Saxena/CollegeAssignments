all: l3a l3b l3c l3d timing 
make target NODES 

l3a: l3a.py
 python l3a.py DelayedFlights.csv NODES 

l3b: l3b.py
 python l3b.py DelayedFlights.csv NODES

l3d: l3d.py
 python l3d.py DelayedFlights.csv NODES

timing: timing.pyc
 python timing.py DelayedFlights.csv NODES
