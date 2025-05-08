import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
#case valor:


# linguagem = 100

# match linguagem:
    
#     case "python":
#         print("É fácil")
#     case "java":
#         print("Muito código, python faz com linhas menores")
#     case "c#":
#         print("Massa")
#     case "js":
#         print("Sou do back")
#     case "html":
#         print("Kauan não dorme")
#     case 10:
#         print("Entrou aqui!")
#     case _ :
#         print("Outro caso")

#atividade dos dias da semana:
# print("TABELA DOS DIAS DA SEMANA:")
# print("1: Domingo")
# print("2: Segunda")
# print("3: Terça")
# print("4: Quarta")
# print("5: Quinta")
# print("6: Sexta")
# print("7: Sábado")
# dia = int(input("Digite o número do dia da semana: "))


# match dia:

#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda")
#     case 3:
#         print("Terça")
#     case 4:
#         print("Quarta")
#     case 5:
#         print("Quinta")
#     case 6:
#         print("Sexta")
#     case 7:
#         print("Sábado")

#atividade da loja de celular
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

# Desenhos pedra papel tesoura

# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

#MINHA RESPOSTA:
import random

pedra = (r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

papel = (r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

tesoura = (r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("JOGO PEDRA PAPEL TESOURA")
usuario = input("Digite pedra ou papel ou tesoura:").lower()
numero = random.randint(0, 2) #gera de 0 até 2 aleatoriamente

match numero:
    case 0:
        maquina = "pedra"
    case 1:
        maquina = "papel"
    case 2:
        maquina = "tesoura"

print("\nMáquina:", maquina)
match maquina:
    case "pedra":
        print(pedra)
    case "papel":
        print(papel)
    case "tesoura":
        print(tesoura)

print("Você:", usuario)
match usuario:
    case "pedra":
        print(pedra)
    case "papel":
        print(papel)
    case "tesoura":
        print(tesoura)

match (usuario, maquina):
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("VOCÊ GANHOU!")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("VOCÊ PERDEU!")
    case _:
        print("EMPATE!")



#correção do professor -> primeiro modo:
print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador = pedra
    case "tesoura": 
        jogador = tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura

maquina = random.randint(1,3)

match maquina:
    case 1:
        maquina = pedra
    case 2: 
        maquina = papel
    case 3:
        maquina = tesoura


print(f"Você escolheu:  {jogador}")
print(f"Máquina escolheu: {maquina}")

match jogador:
    case _ if jogador == maquina:
        print("EMPATE")
    case _ if jogador == pedra and maquina == tesoura:
        print("Você ganhou!")
    case _ if jogador == tesoura and maquina == papel:
        print("Você ganhou!")
    case _ if jogador == papel and maquina == pedra:
        print("Você ganhou!")
    case _ :
        print("Você perdeu!")



#correção do professor -> segundo modo:
print("JOGO PEDRA PAPEL TESOURA ")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#pedra=1 papel=2 tesoura=3
mao = input("Digite pedra ou papel ou tesoura :")
maquina = random.randint(1,3)

match maquina :
    case 1:
        maquina = "pedra"
    case 2:
        maquina = "papel"
    case 3 :
        maquina = "tesoura"

match mao:

    case _ if mao == "pedra" and maquina == "pedra" :
        print(f"Máquina: {maquina} {pedra}")
        print(f"Você: {mao}  {pedra}")
        print("EMPATOU!")
    
    case _ if mao == "pedra" and maquina == "papel":
        print(f"Máquina: {maquina} {papel}")
        print(f"Você: {mao}  {pedra}")
        print("PERDEU!")
    case _ if mao == "pedra" and maquina == "tesoura":
        print(f"Máquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {pedra}")
        print("GANHOU!")
    case _ if mao == "papel" and maquina == "papel":
        print(f"Máquina: {maquina} {papel}")
        print(f"Você: {mao}  {papel}")
        print("EMPATOU!")
    case _ if mao == "papel" and maquina == "pedra":
        print(f"Máquina: {maquina} {pedra}")
        print(f"Você: {mao}  {papel}")
        print("GANHOU")
    case _ if mao == "papel" and maquina == "tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {papel}")
        print("PERDEU!")
    case _ if mao == "tesoura" and maquina == "pedra":
        print(f"Máquina: {maquina} {pedra}")
        print(f"Você: {mao}  {tesoura}")
        print("PERDEU!")
    case _ if mao == "tesoura" and maquina == "papel":
        print(f"Máquina: {maquina} {papel}")
        print(f"Você: {mao}  {tesoura}")
        print("GANHOU!")
    case _ if mao == "tesoura" and maquina == "tesoura":
        print(f"Máquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {tesoura}")
        print("EMPATOU!")
    case _:
        print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA.")


