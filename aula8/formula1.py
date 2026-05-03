import csv
corridas = []

with open ("winners.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    corridas.append(linha)

# print(corridas[0])
# print(corridas[0]['Winner'])

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def totaliza_vitorias():
  vitorias = {}
  
  for piloto in corridas:
    cat = piloto["Winner"]
    vitorias[cat] = vitorias.get(cat, 0) + 1
    vitorias = dict(sorted(vitorias.items(),key=lambda, reverse=True))
  
  print(vitorias)

while True:
   titulo("Pilotos de Fórmula 1: Exemplos de Análises")
   print("1. Análise por Nº de corridas")
   print("2. ...... ")
   print("3. ...... ")
   print("4. Finalizar")
   opcao = int(input("Opção: "))
   if opcao == 1:
     totaliza_vitorias()
   # elif opcao == 2:
   #   top10_idosos()
   # elif opcao == 3:
   #   analise_classe()
   else:
     break