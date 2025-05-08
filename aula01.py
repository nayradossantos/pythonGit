#aula 01 -> marcadores
print(" HELLO WORLD! ")
print(" Nayra ")
#diferença entre texto e numero
print(10+10) #realiza a soma 10+10=20
print("10"+"10") # concatena = junta 10 com 10 = 1010

#operações matemáticas
#soma +
#subtração -
#mutiplicação *
#divisão /

#exemplos
print(2+2)
print(10-5)
print(10*2)
print(20/2)

#PARAMETROS NO PRINT
print("a,b,c,d,e....") #até no máximo 128 parametros
print("escola senai")
print("escola","senai")
print("10 + 10 =", 10+10)

#atividade 1
print("Nayra Monteiro dos Santos , 16  , 492.011.498.24")
print("Nayra Monteiro dos Santos",16,49201149824)

#formatações Sep e End
#sep -> operador de separação
#troca o caractere padrão na vírgula pelo setado dentro do sep
#end -> operador final
#coloca o caractere no final do print
#\n -> quebra a linha; onde coloca "\n" ele quebra a linha
#limpar a tela
import os
os.system("cls")

# print("-"*5,"ATIVIDADE 1", "-"*5)
print("aula" , "de" , "python", sep="@",end="! \n") #@/!: pode ser qualquer símbolo ou palavra
print("no senai")

#print("outro \nexemplo")

# #SEP e END - atividade 1
print("curso" , "de" , "python", sep="_",end="%% \n")
print("*no senai rio claro")
print("_-"*2 , "logica", "-_-" , "de" , "-_-" , "programação" , sep="_")
print("\n")
print("-"*5,"ATIVIDADE 2", "-"*5)
#SEP e END - atividade 2
print("python" , "versao3" , sep="@"*3 , end="[] \n")
print("logica" , "de" , "programação", sep="#"*3)
print("&" "uso" "&" "do" "&" "print" "()")
