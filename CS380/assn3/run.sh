#!/bin/sh
if [ "$#" -gt 1 ]; then
    python3 connect3.py "$1" "$2"
else
    python3 connect3.py "$1"
fi
