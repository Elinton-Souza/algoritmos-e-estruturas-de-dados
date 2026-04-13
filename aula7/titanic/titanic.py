import csv

# lista dos passageiros (lista de dicionários)
titanic = []
sexo = []

# lê os dados do arquivo e insere-os na lista
with open("train.csv") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    titanic.append(linha)

# print(titanic[0])
# print(titanic[0]['Name'])

def titulo(texto, traco="-"):
  print()
  print(texto.upper())
  print(traco*40)

def dados_sexo():
  titulo("Passageiros por Sexo e Sobreviventes")
  
  # Masculino: xxx
  # - sobreviventes: xx
  # - Mortos: xx
  
  # Feminino: xxx
  # - sobreviventes: xx
  # - Mortos: xx

while True:
  titulo("Passageiros do Titanic", "=")
  print("1. Dados por Sexo e Sobreviventes")
  print("2. Média de Idade e Mais Idosos(Top 10)")
  print("3. Dados por Classe e Sobreviventes")
  print("4. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    dados_sexo()
  else:
    break
