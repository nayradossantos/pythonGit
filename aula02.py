import os
os.system("cls")
#aula02 -> variaveis, tipos e input
#Tipos de Dados
#String -> Texto
#Int -> Inteiro
#Float -> Quebrado (flutuante)

#declaração de variáveis
escola = "senai"
#mostrando o valor da variavel no print
#concatenando com o +
print("o nome da minha escola é " + escola)
#separando por parametro ,
print("o nome da minha escola é" , escola)
#f string {} -> mostra o valor da variavel dentro das aspas
print(f"o nome da minha escola é {escola}")

#exemplo de variavel int
numero = 100
print("somando com 10 = ",numero+10)
print("subtraindo 5 = ", numero -5)
print("dividindo por 2 = ", numero/2)
print("multiplicando por 10 = ", numero *10)

#atividade
print("-"*5,"DADOS", "-"*5)
nome = "Nayra"
idade = 16
CPF = 49201149824
print("Meu nome é " + nome)
print("Minha idade é " ,idade)
print("Meu CPF é " ,CPF)

#input
#Obrigatoriamente antes do input deve existir uma variável
#resumido...
#input() -> pergunta algo a ser armazenado
#print() -> mostra texto na tela

texto = input("digite algo: ")
print("você digitou ... " ,texto)

#atividade
print("*"*10,"CADASTRO", "*"*10)
nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
rg = input("Digite rg: ")
print("*"*10,"DADOS CADASTRADOS", "*"*10)
print("NOME:" ,nome)
print("CPF:" ,cpf)
print("RG:" ,rg)
print("*"*10, "DADOS CADASTRADOS","*"*10)
print("NOME: ", nome)
print("CPF: " + cpf)
print(f"RG: {rg} ")