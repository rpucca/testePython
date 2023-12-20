idade = int(input('Digite idade'))
if (idade%2) == 0:
    print('Idade par')
else:
    print('Idade impar')

if 0 <= idade <= 12:
    print('Criança: 0 a 12 anos')
elif 13 <= idade <= 18:    
    print('Adolescente: 13 a 18 anos')
elif idade >= 18:        
    print('Adulto: acima de 18 anos')    

