import os
os.system('cls')

membros = int(input('Digite a quantidade de membors no grupo:  '))
membros1 = membros
idade1 = 0
idade = 0

while membros>0:

    idade = int(input('Digite a idade do proximo membro:  ')) 
    idade1 = idade1 + idade
    membros = membros - 1


mediaIdade = idade1 / membros1

if(mediaIdade<26):
    {
        print('O grupo é JOVEM, com a media de idade de ', mediaIdade,' anos')
    }
elif(mediaIdade<61):
    {
        print('O grupo é ADULTO, com a media de idade de ', mediaIdade,' anos')
    }
else:    
    {
        print('O grupo é IDOSO, com a media de idade de ', mediaIdade,' anos')
    }

    