import random
import time
from colorama import init, Fore

#Inicializa o Colorama
init(autoreset=True)

print(Fore.BLUE + "===  JOGO DESCUBRA A PALAVRA ===")
nome = input(Fore.YELLOW + "Nome do Jogador: ")

tempo_inicial = time.time()

palavras = []
dicas = []
erros = 0
max_erros = 6

def carregar_palavras():
  try:
    with open("palavras.txt", "r", encoding="utf-8") as arq:
      dados = arq.readlines()
      for linha in dados:
        partes = linha.split(";")
        palavras.append(partes[0])
        dicas.append(partes[1])
  except FileNotFoundError:
    print(Fore.RED + "Arquivo palavras.txt não encontrado")
    exit(1)       #1: Indica saída por erro de execução

carregar_palavras()
#print(palavras)
#print(dicas)

num = random.randint(0, len(palavras)-1)

palavra = palavras[num]
dica = dicas[num]

letras_usadas = [palavras[0]]
palavra_escondida = ["_"]* len(palavra)

for i in range(0, len(palavra)):
  if palavra[i] == palavra[0]:
    palavra_escondida[i] = palavra[0]

#print(palavra_escondida)

carinhas = [
  "😀😀😀😀😀",
  "😡😀😀😀😀",
  "😡😡😀😀😀",
  "😡😡😡😀😀",
  "😡😡😡😡😀",  
  "😱😱😱😱😱"
]

def mostrar_status():
  print(Fore.MAGENTA + f"Status: {carinhas[erros]}")
  print(Fore.YELLOW + f"Palavra: {' '.join(palavra_escondida)}")
  print(Fore.RED + f"Erros: {erros}/{max_erros}")

while True:
  #Verifica se ganhou (palavra_escondida == palavra)
  if "".join(palavra_escondida) == palavra:
    print(Fore.GREEN + f"Parabéns {nome}! Você venceu 🎉🎉")
    break

  #Verifica se perdeu
  if erros == max_erros:
    print(Fore.RED + f"Bah, {nome}. Você perdeu! 🤬🤬 A Palavra era {palavra}")
    break

  mostrar_status()

  letra = input("\nLetra ou * para ver dica (vale 1 vida): ").upper()

  if letra == "*":
    if "*" in letras_usadas:
      print(Fore.RED + "Dica já usada")
    else:
      print(Fore.YELLOW + f"Dica: {dica}")
      erros += 1
      letras_usadas.append("*")
    continue

  if letra in letras_usadas:
    print(Fore.RED + "Letra ja usada")
    continue

  letras_usadas.append(letra)

  if letra in palavra:
    print(Fore.GREEN + f"Letra '{letra}' encontrada!")
    for i in range(len(palavra)):
      if palavra[i] == letra:
        palavra_escondida[i] = letra   
  else:
    erros += 1
    print(Fore.RED + f"Letra '{letra}' não existe na palavra...")

tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(Fore. YELLOW + f"Jogo durou: {duracao:.2f} segundos")