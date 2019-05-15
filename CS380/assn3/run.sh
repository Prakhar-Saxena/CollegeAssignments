#!/bin/sh
if [ "$#" -gt 1 ]; then
    python3 Main.py "$1" "$2"
else
    python3 Main.py "$1"
fi
