#se executar no terminal o comando "python codigo02.py", esse será o codigo principal executado, ou seja, o MAIN identificado pelo python, 
#o codigo irá importar o codigo01.py que NÃO é o codigo MAIN identificado pelo python,
#então NÃO exibirá no codigo01.py o comando print dentro do if __name__ == '__main__':'''
#e exibirá aqui no codigo02.py    o comando print dentro do if __name__ == '__main__':'''
import codigo01
print('Estou no codigo02')
if __name__ == '__main__':
    print('Executei no terminal o comando python codigo02, logo esse é o __main__') 