import os

#restaurante_array = ['Pizza','Sushi']
restaurante_array = [ {'nome':'Pizza',  'categoria':'Pizza'   , 'ativo': False},
                      {'nome':'Shushi', 'categoria':'Italiano', 'ativo': True},
                      {'nome':'Tartai', 'categoria':'Espanhol', 'ativo': False},
                      {'nome':'x'     , 'categoria':'y'       , 'ativo': False}                      
                    ]
                                        
def opcoes_exibir():    
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Alterar Status Restaurante')
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
                restaurante_alterar_status()
            case 4:
                app_finalizar()
            case _:
                opcao_invalida()
    except:
            opcao_invalida()

def titulo_exibir(texto):    
    os.system('cls')
    linha = '*' * (len(texto))
    print(f'{linha}\n{texto}\n{linha}') 
    print()   

def menu_voltar():
    input('\nDigite uma tecla para voltar ao menu.')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    menu_voltar()

def restaurante_cadastrar():
    titulo_exibir('Cadastrar restaurante')    
    var_nome      = str(input('Nome do restaurante:'))
    var_categoria = str(input(f'Categoria do restaurante {var_nome}:'))

    restaurante_array.append({'nome':var_nome,'categoria':var_categoria,'ativo':False})

    print(f'O restaurante {var_nome} foi cadastrado.')
    menu_voltar()

def restaurante_listar():
    titulo_exibir('Listar restaurante')
    
    print(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante_item in restaurante_array:
        var_nome      = restaurante_item['nome']
        var_categoria = restaurante_item['categoria'] 
        var_status = 'ativo' if restaurante_item['ativo'] else 'desativado'

        print(f'{var_nome.ljust(20)} | {var_categoria.ljust(20)} | {var_status}')
    menu_voltar()        

def restaurante_alterar_status():
    titulo_exibir('Alterar status restaurante')
    var_nome = str(input('Qual restaurante vc quer alterar status?'))
    var_achou = False

    for restaurante_item in restaurante_array:
        if var_nome == restaurante_item['nome']:
            var_achou = True
            restaurante_item['ativo'] = not restaurante_item['ativo']
            print(f'O status do restaurante {restaurante_item['nome']} foi alterado de {not restaurante_item['ativo']} para {restaurante_item['ativo']}.')
        
            teste = 'ativado' if  restaurante_item['ativo'] else 'desativado'
            print(f'teste:{teste}')

    if not var_achou:
        print('Esse nome não existe!')

    menu_voltar()        

def app_finalizar():
    titulo_exibir('Fim do app')

def main(): 
    print('''
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
