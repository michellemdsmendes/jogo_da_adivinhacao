from random import randint
computador = randint(0,10) # faz o computador "PENSAR"
print('Sou o seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente outra vez.')
        elif jogador > computador:
            print('Menos.. Tente mais vez.')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpites))