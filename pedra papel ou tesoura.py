while True:
    vc = str(input('Pedra, Papel ou Tesoura? \n'))
    if vc == 'Pedra' or vc == 'pedra':
        print('Você escolheu Pedra')
        break
    elif vc == 'Papel' or vc == 'papel':
        print('Você escolheu Papel')
        break
    elif vc == 'Tesoura' or vc == 'tesoura':
        print('Você escolheu Tesoura')
        break
    
#escolha pc
import random

pc = random.randrange(1,4)

if pc == 1:
    print('\nO computador escolheu Pedra')
elif pc == 2:
    print('\nO computador escolheu Papel')
elif pc == 3:
    print('\nO computador escolheu Tesoura')

if pc == 1 and vc == 'Pedra':
    print('\n Empate')
elif pc == 2 and vc == 'Papel':
    print('\n Empate')
elif pc == 3 and vc == 'Tesoura':
    print('\n Empate')

elif pc == 1 and vc == 'Tesoura':
    print('\n Você perdeu')
elif pc == 2 and vc == 'Pedra':
    print('\n Você perdeu')
elif pc == 3 and vc == 'Papel':
    print('\n Você perdeu')
    
elif pc == 1 and vc == 'Papel':
    print('\n Você ganhou!')
elif pc == 2 and vc == 'Tesoura':
    print('\n Você ganhou!')
elif pc == 3 and vc == 'Pedra':
    print('\n Você ganhou!')
#============================================#
if pc == 1 and vc == 'pedra':
    print('\n Empate')
elif pc == 2 and vc == 'papel':
    print('\n Empate')
elif pc == 3 and vc == 'tesoura':
    print('\n Empate')

elif pc == 1 and vc == 'tesoura':
    print('\n Você perdeu')
elif pc == 2 and vc == 'pedra':
    print('\n Você perdeu')
elif pc == 3 and vc == 'papel':
    print('\n Você perdeu')
    
elif pc == 1 and vc == 'papel':
    print('\n Você ganhou!')
elif pc == 2 and vc == 'tesoura':
    print('\n Você ganhou!')
elif pc == 3 and vc == 'pedra':
    print('\n Você ganhou!')
