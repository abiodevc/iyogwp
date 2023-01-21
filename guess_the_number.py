from random import randint

def main():
    print('''|---------------------------------|
|jogo de adivinhar o numero blabla|
|---------------------------------|''')
    print('digite seu chute:')

    num = randint(0, 99)
    gameon = True
    tries = 0

    while gameon:
        tries += 1
        player = int(input(''))
        if player == num:
            print('parabens!! voce acertou.')
            print(f'numero de tentativas: {tries}')
            gameon = False
        elif player > num:
            print('voce errou, chutou um numero muito alto.')
            print('tente novamente!!')
        elif player < num:
            print('voce errou, chutou um numero muito baixo.')
            print('tente novamente!!')

main()