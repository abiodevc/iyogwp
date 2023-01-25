from os import name, system
from time import sleep
from lista_palavras import listapalavras
from desenho import forcafun

#função para limpar tela, coloquei condiçao para poder limpar windows e linux
def clear():
    if name == 'nt':
        cleaning = system('cls')
    else:
        cleaning = system('clear')

def desenha(a, b, c):
    clear()
    forcafun(a, b, c)
