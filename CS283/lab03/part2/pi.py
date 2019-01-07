#!/usr/bin/env python

import random

num_samples = 100
num_of_nodes = 4

def inside(p):     
	x, y = random.random(), random.random()
	return x*x + y*y < 1

count = sc.parallelize(range(0, num_samples), num_of_nodes).filter(inside).count()

pi = 4.0 * count / num_samples
print(pi)

sc.stop()
