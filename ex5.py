import os
os.system('cls')


opcao = 0


print('Inofrme as notas 3 do aluno, ou digite 99 para sair')

while opcao!=99:

    nota1 = float(input('Nota 1: '))
    if(nota1==99):
        opcao=99
        break

    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))   

    notas = [nota1, nota2, nota3]

    media = sum(notas) / len(notas) #SUM É A SOMA DAS NOTAS, LEN É QUANTIDADE DE NOTAS - descoberta nova (y)

    if(media==10):
        print(f"Aluno aprovado com distinção, com media {media:.2f}" )
    
    elif(media>=7):
        print(f"Aluno aprovado, com media {media:.2f}")

    else:
        print(f"Reprovado, com media {media:.2f}")

print('********Finalizado!!********')