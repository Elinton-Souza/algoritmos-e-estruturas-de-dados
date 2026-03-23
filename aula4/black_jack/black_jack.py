import random
import time
import sys

naipes = "♠♥♦♣"
extras = "JQKA"

# Baralho deve ter todas as cartas a serem sorteadas
baralho = []

# def: função definida pelo usuário
def monta_baralho():
  # monta o baralho do 2 ao 10, com todos os naipes
  for i in range(2, 11):
    for naipe in naipes:
      baralho.append(str(i)+naipe) #"2♠️", "@2.."

  # Adiciona os símbolos extras JQKA com os naipes
  for extra in extras:
    for naipa in naipes:
      baralho.append(extra+naipe)

# chama a função
monta_baralho()
# print(baralho)

def verifica_pontos(carta):
  if len(carta) == 3:       # só pode ser 10♠, 10♥, 10♦, 10♣
    num = 10
  elif carta[0].isdigit():  # se é dígito numérico
    num = int(carta[0])
  elif carta[0] == "A":     #símbolos: A vale 11
    num = 11
  else:
    num = 10                # outros símbolos valem 10
  return num

pontos_jogador = 0          # Acumula pontos do jogador
contador = 0
# Geração das Cartas para o Apostador
while True:
  # Gera número aleatório entre 0 e tamanho do baralho-1
  num = random.randint(0, len(baralho)-1)
  # pop: remove um elemento da lista (vetor)
  carta = baralho.pop(num)
  
  contador +=1
  print(f"Sua {contador}ª Carta é: {carta}")
  time.sleep(2)

  pontos_jogador += verifica_pontos(carta)
  
  if pontos_jogador >= 21:
    break

  if contador >= 2:
    outra = input("Deseja outra carta (S/N): ").upper()
    if outra == "N":
      break

print()
print("*"*44)
print()
print(f"  ==>  Total de Pontos do Jogador: {pontos_jogador}")
print()
print("*"*44)
print()
print()

if pontos_jogador > 21:
  print("Bah... Você perdeu! Tente outra vez 😒😥😂")
  print()
  print("*"*44)
  print()
  sys.exit()    # sai do programa


###############################

pontos_pc = 0          # Acumula pontos do pc
contador = 0
# Geração das Cartas para o pc
while True:
  # Gera número aleatório entre 0 e tamanho do baralho-1
  num = random.randint(0, len(baralho)-1)
  # pop: remove um elemento da lista (vetor)
  carta = baralho.pop(num)
  
  contador +=1
  print(f"A {contador}ª Carta do Computador é: {carta}")
  time.sleep(2)

  pontos_pc += verifica_pontos(carta)
  
  if pontos_pc > 21 or pontos_pc >= pontos_jogador:
    break

print()
print("*"*44)
print()
print(f" ==>   Total de Pontos do pc: {pontos_pc}")
print()
print("*"*44)
print()
print()
if pontos_pc > 21:
  print("Parabéns! Você venceu! 🎉")
  print()
  print("*"*44)
  print()
elif pontos_pc == pontos_jogador:
  print("Oh... Deu Empate! 🤗")
  print()
  print("*"*44)
  print()
else:
  print("Bah... Você perdeu. 🤬")
  print()
  print("*"*44)
  print()
