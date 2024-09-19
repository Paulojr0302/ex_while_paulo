from os import system
import os
os.system('cls')

num = int(input('Digite qualquer numero: '))
quantidade1 = 0
quantidade2 = 0
quantidade3 = 0
quantidade4 = 0

while num>0:
    
    if(num<26):
            quantidade1 = quantidade1+1
        
    elif(num<51):
            quantidade2 = quantidade2 + 1

    elif(num<76):
            quantidade3 = quantidade3 + 1
        
    elif(num<101):
            quantidade4 = quantidade4 + 1
    
    num = int(input('Digite qualquer numero:  '))


print(quantidade1,'numeros de 0 - 25 *** ', quantidade2 ,' numeros de 26 - 50 ***' , quantidade3,' numeros de 51 - 75 *** ', quantidade4, ' numeros de 76 - 100')    
