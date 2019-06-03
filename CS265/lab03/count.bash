#!/bin/bash
#
# Prakhar Saxena
# 2018-04-20
# 

for entry in ./*
do
	printf "${entry##*/} "
	wc -lw < "$entry"	
done

exit 0
