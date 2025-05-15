#Estrutura de repetição while (enquanto)
#enquanto uma condição for verdadeira ele
#executa o looping até que ela seja falsa

# aula = 8
# while aula == 8:
#     print("silêncio!")
#     aula = 9
# else:
#     print("é executado quando o while é falso")

# #while incremental
# i = 0

# while i < 10:
#     i = i+1 #incrementar de 1 em 1
#     i+=1 #incremento simplificado mesma coisa que i = i+1
#     print("valor da variável =", i)

#atividade 1:
# i=1
# while i < 18:
#     i+=1
#     print("Valor da variável:", i)

#CORREÇÃO:
# x=2

# while x <19:
#     print(x)
#     x+=1

#atividade 2:
# i=1
# while i > -50:
#     i-=1
#     print("Números:", i)

#CORREÇÃO:
# x=0

# while x >-51:
#     print(x)
#     x-=1

# atividade 3:
# print("*"*15, "PROGRAMA DE CADASTRO", "*"*15)
# print("""
# 1- Cadastrar o nome:
# 2- Cadastrar o CPF:
# 3- Cadastrar a idade:
# 4- Sair do programa
# """)

# opcao = 0

# while opcao != 4:
#     opcao = int(input("Digite uma opção:"))

#     if opcao == 1:
#         nome = input("Digite o nome:")
#     elif opcao == 2:
#         cpf = input("Digite o CPF:")
#     elif opcao == 3:
#         idade = int(input("Digite sua idade:"))
#     elif opcao == 4:
#         print("Dados cadastrados:")
#         print(f"Nome: {nome}")
#         print(f"CPF: {cpf}")
#         print(f"Idade: {idade}")
#     else:
#         print("Opção inválida!")


# #ATIVIDADES COM WHILE (fácil):
# #atividade 1:
# print("*"*15, "Programa: senha", "*"*15)

# senha = 1505

# while senha == 1505:
#     senha = int(input("Digite uma senha:"))

#     if senha == 1505:
#         print("Senha correta" "\nVocê entrou!")
#     elif senha == 9999:
#         print("Programa encerrado!")
#     else:
#         print("Senha incorreta" "\nTente novamente")
#         senha = 1505


# # atividade 2:
# import random

# print("Jogue com a Máquina")

# numero = 0
# computador = random.randint(1,10)

# while numero != computador:
#     computador = random.randint(1,10)
#     numero = int(input("Escolha um número de 1 até 10:"))
#     print("Você escolheu:", numero)
#     print("Computador escolheu:", computador)

#     if numero != computador:
#         print("Número incorreto!" "\nTente novamente")
#     if numero == computador:
#         print("Número correto!")


# # atividade do caixa eletrônico:
# print("="*15, "MENU", "="*15)
# print("""
# DIGITE 1 - Realizar depósito 
# DIGITE 2 - Realizar saque
# DIGITE 3 - Saldo
# DIGITE 4 - Sair
# """)

# saldo = 0
# opcao = ""

# while saldo != 4:
#     opcao = int(input("\nDigite a opção desejada: "))
#     if opcao == 1:
#         deposito = float(input("Digite o valor do depósito R$:"))
#         saldo = saldo+deposito
#     elif opcao == 2:
#         saque = float(input("Digite o valor do saque R$:"))
#         saldo = saldo-saque
#     elif opcao == 3:
#         print("SALDO R$:", saldo)
#     elif opcao == 4:
#         print("Saiu do programa")
#         break


#atividade guanabara:
# print("="*36)
# print("="*15, "MENU", "="*15)
# print("="*36)

# print("""
# DIGITE 1 - Somar 
# DIGITE 2 - Multiplicar
# DIGITE 3 - Maior
# DIGITE 4 - Novos números
# DIGITE 5 - Sair do programa
# """)


# valor1 = float(input("Digite o primeiro valor:"))
# valor2 = float(input("Digite o segundo valor:"))
# opcao = 0
# print("------------------------------")

# while opcao != 5:
#     opcao = int(input("Digite a opção desejada:"))

#     if opcao == 1:
#         somar = valor1 + valor2
#         print(f"O resultado é: {valor1} + {valor2} = {somar}")
#     elif opcao == 2:
#         multiplicar = valor1 * valor2
#         print(f"O resultado é: {valor1} * {valor2} = {multiplicar}")
#     elif opcao == 3:
#         maiornum = max(valor1,valor2)
#         print(f"O maior número é: {maiornum}")
#     elif opcao == 4:
#         valor3 = float(input("Digite um novo número:"))
#         valor4 = float(input("Digite um outro número:"))
#         valor1 = valor3
#         valor2 = valor4
# else:
#     print("Você saiu do programa.")


#atividade de conversão:
print("CALCULADORA DE NOTAS")
print("CONVERSÃO DO VALOR EM NOTAS DE 100, 50, 20, 10, 5 e 1")
print("Digite um valor diferente de -1 para continuar fazendo a conversão!")
print("-"*67)
while True:
    valor = int(input("Digite o valor que deseja sacar em cédulas:"))
    if valor == -1:
        print("Você saiu do programa")
        break
    
    notas = (100,50,20,10,5,1)

    print("Quantidade de notas:")

for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota}")

print("-"*67)