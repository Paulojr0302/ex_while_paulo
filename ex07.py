import os
os.system('cls')

print('Digite a região em que as vendas serão calculadas, e os valores dos 4 meses')
regiao = 'a'

while regiao!='encerrar':

    regiao = input('Digite a REGIÃO:  ')
    if(regiao == 'encerrar'):
        break

    jan = float(input('Digite os valores das vendas de JANEIRO:  '))
    jan = jan*0.1
    fev = float(input('Digite os valores das vendas de FEVEREIRO:  ' ))
    fev = fev*0.4
    mar = float(input('Digite os valores das vendas de MARÇO:  ' ))
    mar = mar*0.4
    abr = float(input('Digite os valores das vendas de ABRIL:  ' ))
    abr = abr*0.1

    meses = [jan, fev, mar, abr]

    media = sum(meses)

    print(f"Região: {regiao}, Media de vendas: {media:.2f}")

print('************FINALIZADO!!************')
    

