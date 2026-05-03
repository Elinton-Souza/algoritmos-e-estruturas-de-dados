import csv
visitantes = []

with open("Number of foreign visitors to Japan by month_ .csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    visitantes.append(linha)

# print(visitantes[0])
# print(visitantes[0]['Country'])

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def num_paises():
  titulo("Nº de Países Analisados")
  
  paises = set()
  for visitante in visitantes:
    paises.add(visitante['Country'])

  numero = len(paises)
  print(f"Nº de países diferentes: {numero}")

  paises = set([p['Country'].strip() for p in visitantes if p.get('Country')])
  print(f"Nº de países diferentes: {len(paises)}")

def top10_paises():
  titulo("Top 10 Países com Maior Nº de Visitantes")

  grupos = {}

  for visitante in visitantes:
    pais = visitante['Country']
    num = int(visitante['Visitor'])
    # grupos.get() obtém o valor da chave pesquisada ou 0 se nao existir
    grupos[pais] = grupos.get(pais, 0) + num

  #Ordena por valor
  grupos2 = dict(sorted(grupos.items(), key=lambda grupo: grupo[1], reverse=True))

  print("Nº Pais..........................: NºVisitantes:")
  print("------------------------------------------------")

  for x, (pais, numero) in enumerate(grupos2.items(), start=1):
    print(f"{x:2d} {pais:30s} {numero:13d}")
    if x == 10:
      break


def acima_100_mil():
  

# def analise_sexo():
#   titulo("Análise por Sexo")

#   masc = 0
#   fem = 0

#   for pessoa in titanic:
#     if pessoa['Sex'] == "male":
#       masc += 1
#     elif pessoa['Sex'] == "female":
#       fem += 1
  
#   # ----- outra forma (list comprehension)
#   masc_sobre = len([pessoa for pessoa in titanic 
#                 if pessoa['Sex'] == "male" and pessoa['Survived'] == '1'])
#   fem_sobre = len([pessoa for pessoa in titanic 
#                if pessoa['Sex'] == "female" and pessoa['Survived'] == '1'])

#   print(f"Homens: {masc}")
#   print(f" - Sobreviventes: {masc_sobre}")
#   print(f" - Mortos: {masc-masc_sobre}")
#   print()
#   print(f"Mulheres: {fem}")
#   print(f" - Sobreviventes: {fem_sobre}")
#   print(f" - Mortos: {fem - fem_sobre}")

# def top10_idosos():
#   titulo("Passageiros mais idosos - Top 10")

#   titanic_temp = [x for x in titanic if x['Age'] != '']
#   titanic2 = sorted(titanic_temp, key=lambda pessoa: float(pessoa['Age']), 
#                     reverse=True)

#   print("Nº Nome do Passageiro...............................: Idade Sobrevivente")
  
#   # for x, pessoa in enumerate(titanic2, start=1):
#   #   print(f"{x:2d} {pessoa['Name']:50s} {pessoa['Age']:5s} {'Sim' if pessoa['Survived'] == '1' else 'Não'}")
#   #   if x == 10:
#   #     break

#   for x, pessoa in enumerate(titanic2[0:10], start=1):
#     print(f"{x:2d} {pessoa['Name']:50s} {pessoa['Age']:5s} {'Sim' if pessoa['Survived'] == '1' else 'Não'}")
  
#   # Cálculo da média
#   soma = sum([float(pessoa['Age']) for pessoa in titanic2])
#   num = len(titanic2)
  
#   print()
#   print("-"*40)
#   print(f"Média das Idades: {soma/num:.1f}")
#   print("-"*40)

# def analise_classe():
#   pass

while True:
  titulo("Visitantes do Japão: Exemplos de Análises")
  print("1. Nº Países Analisados")
  print("2. Top 10 Países")
  print("3. +100 mil/mês")
  print("4. Top 10 Países por Ano")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    num_paises()
  elif opcao == 2:
    top10_paises()
  elif opcao == 3:
    acima_100_mil()
  elif opcao == 4:
    top10_ano()
  else:
    break
