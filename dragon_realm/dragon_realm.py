# Nesse jogo, o jogador está em uma terra repleta de dragões. Os 
# dragões todos vivem em cavernas com suas enormes pilhas de tesouros.
# Alguns dragões são amigavéis e compartilham seu tesouro, outros
# dragões têm fome e comem qualquer um que ouse entrar na sua caverna.
# O jogador se aproxima de duas cavernas, uma com um dragão amigável e
# outra com um dragão faminto, mas ele não sabe qual dragão está em
# qual caverna. O jogador tem que escolher entre as duas.
from random import choice

def main():
    cavernas = ['1', '2']
    gameon = True

    while gameon:
        dragao = choice(cavernas)

        print('''Voce esta em um terra cheia de dragoes. 
Na sua frente você vê duas cavernas. Em uma caverna o dragão
é amigável e vai compartilhar o tesouro dele com você.
O outro dragão é ganancioso e tem fome, ele vai te comer
assim que você entrar na caverna.
Em qual caverna você vai entrar? (1 ou 2)''')
              
        escolha = input('')
        print('''Voce se aproxima da caverna...
Está está muito escuro...''')
              
        if escolha == dragao:
            print('''Um gigante dragão aparece! Felizmente ele
é amigável e deixa você ficar, você ganhar muitos tesouros
e faz um amigo!''')
                  
        else:
            print('''Um gigante dragão aparece! Ele abre sua boca
e acaba com você em uma mordida.
Você morreu.''')

        print('deseja jogar novamente? (s/n)')
        game = input('')
        if game == 'n':
            gameon = False

main()