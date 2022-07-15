frutas = ['Uva','Maçã','Pera','Goiaba','Laranja','Limão']

for x in range(len(frutas)):
    print(frutas[x],x,'\n')

while True:
    a =(input('Escolha a fruta de acordo com o número: \n'))
    if a == 0:
        print('Escolheu Uva')
        break
    elif a == '1':
        print('Escolheu Maça')
        break
    elif a == '2':
        print('Escolheu Pera')
        break
    elif a == '3':
        print('Escolheu Goiaba')
        break
    elif a == '4':
        print('Escolheu Laranja')
        break
    elif a == '5':
        print('Escolheu limão')
        break
    else:
        print('Escolha um número válido')
    


