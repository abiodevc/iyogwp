import time
from os import system

string = 'stringdeteste'
stringa = list(string)
res = ''
i = 0
system('clear')

while i <= len(stringa):
    if i != len(stringa):
        if stringa[i] == stringa[i].upper():
            stringa[i] = stringa[i].lower()
            res = res + stringa[i]
        elif stringa[i] != stringa[i].upper():
            stringa[i] = stringa[i].upper()
            res = res + stringa[i]
        print('\r' + ''.join(stringa), end='')
        time.sleep(0.08)
        i += 1
    else:
        i = 0