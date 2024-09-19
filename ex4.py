from os import system
import os
os.system('cls')

A = 0
B = 0 
C = 0

voto = input('qual seu voto - A - B - C  ')

if (voto == 'A'):
        A=A+1
    
elif(voto=='B'):
        B=B+1

elif(voto=='C'):
        C=C+1

while voto == 'A' or voto == 'B' or voto == 'C':

    voto = input('Digite o próximo voto, ou digite qualuquer outra letra para sair:   ')


    if (voto == 'A'):
        A=A+1
    
    elif(voto=='B'):
        B=B+1

    elif(voto=='C'):
        C=C+1
    
    else:
        print('Os votos foram: ', A , B , C  )



        
        
