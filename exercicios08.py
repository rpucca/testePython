numero_array = [1,2,3,4,5,6,7,8,9,10]
nome_array = ['Ricardo', 'Rafaella', 'Rebecca']
ano_array = ['1970','2023']

def main():
    print('--Array de número')
    for numero in numero_array:
        print(numero)

    print('--Array de string')
    for nome in nome_array:
        print(nome)    

    print('--Array de ano')
    for ano in ano_array:
        print(ano)

    print('--For descrescente')
    for i in range(10, 0, -1):
        print(i)
    
    print('--For soma impares')
    soma_impar = 0
    for numero in range(1,10):        
        if(numero%2!=0):            
            soma_impar+=numero
            print(numero)
    print(soma_impar)
    
    print('--For multiplicador')
    multiplicador = int(input('Digite um número:'))
    for numero in range(1,10):
        print(f'O número {multiplicador} X {numero} = {multiplicador * numero}')

    print('--For divisor')
    divisor = int(input('Digite um número:'))
    try:
        for numero in range(1,10):
            print(f'O número {numero} / {divisor} = {numero / divisor}')
    except Exception as e:
        print(f'erro de divisão: {e}')

main() 
