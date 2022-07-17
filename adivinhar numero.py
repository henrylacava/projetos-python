print('=----------Advinhar número----------=')

print('Tente advinhar um número entre 1 a 10')

import random

numpc = random.randrange(0, 11)

print('\n........')

print('\nNúmero escolhido...\n')

print('\nLembrando que você tem apenas 3 tentativas')

tentativas = 0
while True:
    num = int(input('Qual seu palpite?\n'))
    if num == numpc:
        print('Acertou com',tentativas,'tentativas!')
        break
    elif num > numpc:
        print('Mais baixo')
        tentativas = tentativas + 1
    elif num < numpc:
        print('Mais alto')
        tentativas = tentativas + 1
        
