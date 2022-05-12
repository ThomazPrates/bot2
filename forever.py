#!/usr/bin/python
from subprocess import Popen

while True:
    print("\nIniciando BOT ")
    p = Popen("python3 index.py", shell=True)
    p.wait() 
