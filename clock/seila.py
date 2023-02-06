from art import *
from time import sleep
from os import system

s = 0


for i in range(100):
    system('clear')
    tprint(str(s))
    sleep(1)
    s += 1

