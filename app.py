import os

restaurante_array = ['Pizza','Sushi']

def opcoes_exibir():    
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Ativar Restaurante')
    print('4.Sair\n')

def opcoes_escolher():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        match opcao_escolhida:
            case 1:
                restaurante_cadastrar()
            case 2:
                restaurante_listar()
            case 3:
                print('Ativar restaurante')
            case 4:
                app_finalizar()
            case _:
                opcao_invalida()
    except:
            opcao_invalida()

def titulo_exibir(texto):
    os.system('cls')
    print(texto)
    print()

def menu_voltar():
    input('\nDigite uma tecla para voltar ao menu.')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    menu_voltar()

def restaurante_cadastrar():
    titulo_exibir('Cadastrar restaurante')
    restaurante_nome = str(input('Nome do restaurante:'))
    restaurante_array.append(restaurante_nome)
    print(f'O restaurante {restaurante_nome} foi cadastrado.')
    menu_voltar()

def restaurante_listar():
    titulo_exibir('Listar restaurante')
    for restaurante_nome in restaurante_array:
        print(f'.{restaurante_nome}')
    menu_voltar()        

def app_finalizar():
    titulo_exibir('Fim do app')

def main(): 
    titulo_exibir('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')    
    opcoes_exibir()
    opcoes_escolher()

if __name__ == '__main__':
    main()    

'''pi = 3.14151356
print('O valor arredondado de pi é:', round(pi, 2))
print(f'O valor arredondado de pi é: {pi:.2f}')
print('A','L','U','R','A',sep='\n')

print(f'Opção:{opcao_escolhida}!') #print(f <- interpolação de strings
print(opcao_escolhida==1)
print(type(opcao_escolhida))
print(type(1))

if opcao_escolhida == 1:
    print('Cadastras restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:  
    print('Ativar restaurante')
else:
    app_finalizar()'''
