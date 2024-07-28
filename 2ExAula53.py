"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horas = int(input('Que horas são: '))
    bomdia= 0<= horas<=11
    boatarde = 12<= horas<=17
    boanoite= 18<= horas <=23
    if bomdia:
        print('Bom dia!!')
    elif boatarde:
        print('Boa tarde!!')
    elif boanoite:
        print('Boa noite!!')
    else:
        print('Digite numero entre 0 e 23')
    
except ValueError:
    print('apenas numeros são validos')