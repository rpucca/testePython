import os

def exibir_nome_do_programa():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░     
        ''')

def exibir_opcoes():    
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Ativar Restaurante')
    print('4.Sair\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção:'))
    if opcao_escolhida == 1:
        print('Cadastras restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:  
        print('Ativar restaurante')
    else:
        finalizar_app()

def finalizar_app():
    os.system('cls')
    print('Fim do app\n')
    #return

def main():     
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()    

'''pi = 3.14151356
print('O valor arredondado de pi é:', round(pi, 2))
print(f'O valor arredondado de pi é: {pi:.2f}')
print('A','L','U','R','A',sep='\n')

print(f'Opção:{opcao_escolhida}!') #print(f <- interpolação de strings
print(opcao_escolhida==1)
print(type(opcao_escolhida))
print(type(1))'''
