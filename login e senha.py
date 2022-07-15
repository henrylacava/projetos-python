while True:
    nome = str(input('Login \n'))
    senha = str(input('Senha \n'))
    if nome != senha:
        print('Logado com sucesso!')
        break
    else:
        print('Coloque uma senha diferente do login')

