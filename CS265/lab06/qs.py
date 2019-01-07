#!/usr/bin/env python
#

import sys

def swap(a, b):
	temp = a
	a = b
	b = temp

def partition(a, lo, hi):
	i = lo
	temp = 0;
	pivot = a[lo]
	for j in range(lo, hi-1):
		if a[j] <= pivot:
			i+=1
			swap(a[i], a[j])
		swap(a[i+1], a[hi])
	return i + 1

def quick_sort(a, lo, hi):
	i = partition(a, lo, hi)
	if lo < hi:
		for i in range(0, len(a)-1):
			print a[i], ", "
		
		print "\n"
		p = partition(a, lo, hi)
		quick_sort(a, lo, p-1)
		quick_sort(a, p+1, hi)

def main():
	A = [84, 37, 93, 82, 98, 27, 63, 73, 93, 27, 75, 55, 45, 8]
	p = 0
	q = len(A)-1
	quick_sort(A, p, q)

main()
