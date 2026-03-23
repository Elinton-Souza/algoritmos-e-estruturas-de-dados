import random  #Geração de numeros aleatorios
import time    #Geranciar tempo no programa

nome = input("Nome do apostador: ")
valor = float(input("Valor da aposta: "))

input("Pressione ENTER para Iniciar...")

figuras = "🍇🍓🥝"
# print(figuras[0])
# print(figuras[1])
# print(figuras[2])
jogo = ""
print("Suas apóstas: ", end="")

for i in range(3):
  #Gera um numero aleatorio entre 0 e 2
  num = random.randint(0 ,2)
  print (figuras[num], end="", flush=True)
  time.sleep(1)
  jogo = jogo + figuras[num]

print()

# if jogo[0] == jogo[1] and jogo [0] == jogo[2]:
#   premio = valor * 5
#   print(f"Parabéns {nome}! Você ganhou R$ {premio:.2f} 🤘🏼")
# elif jogo[0] == jogo[1] or jogo [0] == jogo[2] or jogo[1] == jogo [2]:
#   print(f"Bah.. Foi por pouco.. Continue jogando..")
# else:
#   print(f"Todas diferentes... Mas, não desista...")

conjunto = set(jogo)  #Conjunto elimina as duplicidades

if len(conjunto) == 1:
  premio = valor * 5
  print(f"Parabéns {nome}! Você ganhou R$ {premio:.2f} 🤘🏼")
elif len(conjunto) == 2:
  print(f"Bah.. Foi por pouco.. Continue jogando..")
else:
  print(f"Todas diferentes... Mas, não desista...")