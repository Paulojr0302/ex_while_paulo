from os import system
import os
os.system('cls')

media = float(input('Digite uma nota: '))
media1 = 0
semestre = 0

while media>0:
    media1 = media1 + media
    semestre = semestre + 1
    media = float(input('Digitre a proxima nota:  '))

mediafinal = media1 / semestre

print('A media final dos ', semestre, 'semestres foi ', mediafinal)


