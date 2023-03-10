from os import system
from lista_palavras import listapalavras
from desenho import forcafun
from time import sleep

def main():
    
    gameon = 's'
    pontos = 0
    
    while gameon == 's' or gameon == 'S':
        palavra = listapalavras()
        lista_certa = ['_'] * len(palavra)
        lista_errada = []
        lista_todas = []
        homem = 0
        

        while (homem != 6 and ''.join(lista_certa) != palavra):
            system('clear')
            forcafun(homem, lista_certa, pontos)
            tinha = False
            repetida = False
            jogador = input('seu chute: ')

            for j in range(len(lista_todas)):
                if jogador == lista_todas[j]:
                    print('voce ja chutou essa letra')
                    sleep(0.75)
                    repetida = True
            
            if not repetida:
                for i in range(len(palavra)):
                    if jogador == palavra[i]:
                        lista_certa[i] = jogador
                        tinha = True
                lista_todas.append(jogador)
            if not tinha and not repetida:
                lista_errada.append(jogador)
                print(f'a letra {jogador} nao esta na palavra')
                sleep(0.75)
                homem += 1

        if homem == 6:
            print('voce perdeu')
            print(f'a palavra era {palavra}')
        elif ''.join(lista_certa) == palavra:
            system('clear')
            forcafun(homem, lista_certa, pontos)
            print('voce ganhou!')
            print(f'a palavra era {palavra}')
            pontos += 1

        gameon = input('Digite S para jogar novamente, ou somente enter para sair: ')
        sleep(1)

main()