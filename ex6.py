import os
os.system('cls')
cidade='a'

print('Digite o nome da CIDADE, após confirmar digite a temperatura em CELCIUS')

while cidade!='fim':
    cidade = input('Digite o nome da CIDADE:  ')
    if(cidade=='fim'):
        break

    C = float(input('Digite a temperatura em CELCIUS: '))

    F = ((9*C)+160)/5

    print(f"A temperatura em FAHRENHEIT de {cidade} é {F:.2f}ºf")

print('**************FINALIZADO!!**************')