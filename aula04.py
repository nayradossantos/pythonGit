import os
os.system("cls")
#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
# else: 
# print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

#exemplo1
# x=10  
# if  > 1000:
#     print("verdade")
# else:
#     print("falso")

#exemplo2
# nome x = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

# Exercicios - if Else
# parte1
# print("*"*15, "DADOS","*"*15)
# idade = int(input("Idade:"))
# if  idade >= 18:
#     print("MAIOR DE IDADE")
# else:
#     print("MENOR DE IDADE")

# parte2
#dica -> abrir if dentro do else
# idade = int(input("Qual a sua idade: "))
# if idade<0 or idade>120:
#     print("IDADE INVÁLIDA")
# else:
#     if idade >= 18:
#         print("maior idade")
#     else:
#         print("menor de idade")

# parte3
# print("*"*15, "ENTRAR","*"*15)
# email = (input("Digite seu email:"))
# senha = (input("Digite sua senha:"))
# if email == "python@senai.com" and senha == "12345678":
#     print("USUÁRIO AUTENTICADO")
# else:
#     print("USUÁRIO OU SENHA INVÁLIDOS")

#parte4
# print("*"*10,"FEIRA", "*"*10)
# quantidade = int(input("Digite o número de maçãs compradas: "))
# preco1 = 0.25
# preco2 = 0.30
# if quantidade < 12:


#atividade maçãs
# print("*"*5, "FEIRA","*"*5)
# quantidade = int(input("Digite a quantidade de maçãs que deseja levar:"))

# if quantidade < 12 :
#     calculo = quantidade * 0.30
#     print("Você irá pagar (0,30 unidade) R$: " , calculo)
# else :
#     calculo = quantidade * 0.25
#     print("Você irá pagar (0,25 unidade) R$: " , calculo)


#Faça um programa que verifique 
#(usando if e else) se uma letra
#digitada é vogal ou consoante (and or).

#meu programa:
#um dos jeitos de fazer:
# print("*"*15, "VOGAL OU CONSOANTE?","*"*15)
# letra = input("Digite uma letra: ")

# if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U" :
#     print("É VOGAL!")
# else :
#     print("É CONSOANTE!")

#correção do professor:
#outro jeito de fazer:
l = input("Digite uma letra: ").lower()

if l =="a" or l =="e" or l =="i" or l =="o" or l =="u" :
    print("É VOGAL!")
else :
    print("É CONSOANTE!")

#FUNÇÕES NOVAS:
#upper() -> CONVERTER TUDO PARA MAIÚSCULO
#lower() -> CONVERTER TUDO PARA MINÚSCULO

#outro jeito:
l = input("Digite uma letra: ")

if l in "aeiouAEIOU" :
    print("É VOGAL!")
else :
    print("É CONSOANTE!")

#Faça um programa que peça dois
#números ao usuário e mostre
#qual o maior e qual o menor.

#meu programa:
print("*"*15, "MAIOR OU MENOR?","*"*15)
numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro número:"))
if numero1 > numero2 :
    print("O maior número é:" , numero1)
    print("O menor número é:" , numero2)
else :
    print("O maior número é:" , numero2)
    print("O menor número é:" , numero1)