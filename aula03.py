import os
os.system("cls")

# #Continuação Input com Int e Float
# #int() -> converte para inteiro
# #float() -> converte para n quebrado

# #exemplo1
numero = 10
numero2 = input("digite um número: ")
print("o tipo de numero é,", type(numero2))
soma = numero + int(numero2)
print(f"soma de {numero} + {numero2}  = ", soma)

# #exemplo2
num1 = input("digite um numero: ")
soma = float(num1) + 15
print("A Soma de ",num1 , "+", "15" ,"=", soma)

# #exemplo3
n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
soma = n1+n2
print(f"a soma de {n1} + {n2} = ", soma)

# #Exercicios Input com Float e Int() - Logica
# #atividade 1
numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))
multiplicacao = numero1*numero2
print(f"O resultado de {numero1} * {numero2}  = ", multiplicacao)
print("O resultado de", numero1 ,"*",numero2 ,"=", multiplicacao)

#atividade 2
n1 = float(input("Digite um número:"))
sucessor = n1 + 1
antecessor = n1 - 1
print("Sucessor:", sucessor, "\nAntecessor:", antecessor)

#atividade 3
num1 = int(input("Digite o seu ano de nascimento: "))
resposta = int(2025) - (num1)
print(f"Idade:",resposta)

#porcentagem
print("25% de 100 =", 0.25 * 100)
print("4% de 400 =", 0.04 * 400)
print("99% de 1525 =", 0.99 * 1525)

#ATIVIDADE: Escreva um programa em python que leia 2 itens de um supermercado você 
#deve armazenar o nome e o valor do item, no final aplique 10% de desconto no
#primeiro item 25% de desconto no segundo item. Calcule o valor total da 
#compra e mostre o nome e o valor com desconto de cada item
#MINHA RESPOSTA
print("-"*10,"SUPERMERCADO", "-"*10)
produto1 = (input("Digite o produto:"))
valor1 = float(input("Digite o valor do produto:"))
produto2 = (input("Digite o produto:"))
valor2 = float(input("Digite o valor do produto:"))
print("="*10,"CAIXA", "="*10)
desconto1 = 0.10 * valor1
print("O preço do produto com 10% de desconto é: ", valor1-desconto1)
desconto2 = 0.25 * valor2
print("O preço do produto com 25% de desconto é: ", valor2-desconto2)
print("------------------------")
soma = valor1-desconto1+valor2-desconto2
print("TOTAL R$: ", soma)

# #CORREÇÃO DO PROFESSOR:
print("*"*15, "SUPERMERCADO SENAI","*"*15)
prod1 = input("digite o nome do primeiro produto: ")
valor1 = float(input("digite o valor desse produto: "))
prod2 = input("digite o nome do segundo produto: ")
valor2 = float(input("digite o valor desse produto: "))
desconto1 = valor1*0.10
desconto2 = valor2*0.25
valorfinal1 = round(valor1-desconto1,2)
valorfinal2 = round(valor2-desconto2,2)
print("."*20,"CAIXA","."*20)
print(f"{prod1} custa {valor1} com 10% = {valorfinal1}")
print(f"{prod2} custa {valor2} com 10% = {valorfinal2}")
print("."*20,"TOTAL","."*20)
total = valorfinal1+valorfinal2
print(f"TOTAL DA COMPRA -> R$: {total}")
      


#round(valor,qtdCasasDecimais) -> faz o arredondamento dos valores