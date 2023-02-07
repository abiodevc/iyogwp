from art import *
from time import sleep
from os import system


# def parar():
#     go = True
#     if 1:
#         go = False
#         return go
#     else:
#         return go

# def start(a):
#     if parar():
#         return True
#     else:
#         return False

# def zerar(a, b ,c):
#     a = 0
#     b = 0
#     c = 0

def contagem(a, b, c):
    if a == 59:
        a = 0
        b += 1
    if b == 59 and a == 59:
        b = 0
        c += 1
    a += 1
    return [a, b, c]

def desenha(a, b, c, s, m, h):
    if s < 10:
        a = '0' + str(s)
    elif s >= 10:
        a = str(s)

    if m < 10:
        b = '0' + str(m)
    elif m >= 10:
        b = str(m)

    if h < 10:
        c = '0' + str(h)
    elif h >= 10:
        c = str(h)

    sleep(1)
    system('clear')
    tprint(f'\r{c}:{b}:{a}')

def main():
    on = True

    s = '00'
    sec = 0
    m = '00'
    minu = 0
    h = '00'
    hour = 0

    while True:
        sec, minu, hour = contagem(sec, minu, hour)
        desenha(s, m, h, sec, minu, hour)

main()
