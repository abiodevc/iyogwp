from random import randint

def main():
    name = input('Qual o seu nome? ')
    print(f'Ola, {name}, eu estou pensando em um numero entre 1 e 100, tente adivinhar!')

    num = randint(1, 100)
    gameon = True
    tries = 0

    while gameon:
        tries += 1
        player = int(input('seu palpite: '))
        if player == num:
            print('parabens!! voce acertou.')
            print(f'numero de tentativas: {tries}')
            gameon = False
        elif player > num:
            print('seu palpite foi muito alto!')
            print('tente novamente.')
        elif player < num:
            print('seu palpite foi muito baixo!')
            print('tente novamente.')

main()