import time
import sys
from os import system
from art import text2art

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
        # a = text2art(''.join(stringa))
        a = '''  ___    ___       ___    ___       ___   _ 
 / _ \  / _ \  _  / _ \  / _ \  _  / _ \ / |
| | | || | | |(_)| | | || | | |(_)| | | || |
| |_| || |_| | _ | |_| || |_| | _ | |_| || |
 \___/  \___/ (_) \___/  \___/ (_) \___/ |_|'''

        sys.stdout.write(f'\r{a}')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    else:
        i = 0