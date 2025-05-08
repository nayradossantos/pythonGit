import os
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 
# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))
# if idade < 12:
#     print("CRIANÇA")
# if idade < 18:
#     print("ADOLESCENTE")
# if idade < 60:
#     print("ADULTO")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("CRIANÇA")
# elif idade < 18:
#     print("ADOLESCENTE")
# elif idade < 60:
#     print("ADULTO")
# else: 
#     print("IDOSO")


#Escreva um programa em python que pergunte
#2 notas a um aluno e calcule a média:
#média = (nota1+nota2)/2
#Mostre a média e a classificação do aluno:
#Se média menor (<) que 5 -> REPROVADO
#Se média entre 5 e 7 -> EM RECUPERAÇÃO
#Se média maior (>) que 7 -> APROVADO

#meu código
print("-"*5,"MÉDIA", "-"*5)
nota1 = float(input("Digite a 1° nota:"))
nota2 = float(input("Digite a 2° nota:"))
media = (nota1+nota2)/2
if media < 5:
    print("REPROVADO!")
elif media <= 7:
    print("EM RECUPERAÇÃO.")
elif media > 7:
    print("APROVADO!")
print("Sua média é:" , media)

#correção do professor
#replace("valor1","valor2") -> Substitui o valor 1 pelo valor2

n1 = float(input("Digite a 1° nota: ").replace(",","."))
n2 = float(input("Digite a 2° nota: ").replace(",","."))

media = (n1+n2)/2
# :.2f -> formata para 2 casas decimais apenas no fstring:
print(f"Média: {media:.2f}")

if media <5:
    print("REPROVADO")
elif media >=5 and media<=7:
    print("EM RECUPERAÇÃO")
else:
    print("APROVADO")


#Atividade IMC
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso/(altura*altura)
print(f"Seu IMC é: {imc:.2f}")
if imc < 17:
    print("Muito abaixo do peso")
elif imc >=17 and imc<=18.49:
    print("Abaixo do peso")
elif imc >=18.5 and imc<=24.99:
    print("Peso normal")
elif imc >=25 and imc<=29.99:
    print("Acima do peso")
elif imc >=30 and imc<=34.99:
    print("Obesidade I")
elif imc >=35 and imc<=39.99:
    print("Obesidade II")
elif imc > 40:
    print("Obesidade III (mórbida)")


#Atividade
print("*"*30, "REAJUSTE AUTOCAR","*"*30)
print(r"""
              _.-'''''''''''''''''''`.
            .` ,'      ||         | `.`.
          .` ,'        ||         |   `.`.
        .`  /          ||         |  ,' ] `....___
      _`__.'''''''''''''''''''''''`''''''''|..___ `-.._
    .'                  [='                '     `'-.._`.
 ,:/.'''''''''''''''''''|''''''''''''''''''|'''''''''''\'\
  //||    _..._         |                  '    _..._  |)|
 /|//   ,',---.`.       |                  |  .',---.`.\>|
(':/   //' .-. `\\      \_________________/  '/' .-. `\\|_)
 `-...'||  '-'  ||________,,,,,,,,,,,,,,,__.'||  '-'  ||-'
       '.'.___.','                           '.'.___.','
         '-.m.-'                               '-.m.-'

""")
print("*"*78)
print("TABELA DE REAJUSTE DE SALÁRIO:")



