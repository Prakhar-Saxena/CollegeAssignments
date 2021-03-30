#!/bin/sh

if [ "$#" -gt 1 ]; then #number of arguments > 1
	python rushhour.py "$1" "$2"
else
	python rushhour.py "$1"
fi
