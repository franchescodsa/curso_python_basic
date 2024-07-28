"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""
try :
    nome=input('Digite seu nome: ')
    tamanho_nome = len(nome)
    nome_curto= tamanho_nome<=4
    nome_normal= tamanho_nome >=5 and tamanho_nome <6
    
    if tamanho_nome <=1:
        print('Digite mais de uma letra')
    elif nome_curto:
        print('Nome curto')
    elif nome_normal:
        print('Nome normal')
    else:
        print('Nome geande')
        
except ValueError:
    print('Digite apenas letras')