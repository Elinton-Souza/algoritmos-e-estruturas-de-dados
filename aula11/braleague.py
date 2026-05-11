import csv
import plotly.express as px

times = []

with open ("BRA_players.csv", mode='r') as arq:
    dados_csv = csv.DictReader(arq)
    for linha in dados_csv:
        times.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("-"*40)

def topValor():
    titulo("Top 10 Clubes +valiosos")

    grupos={}

    for time in times:
        nome = time['Team']
        valor = float(time['Market Value'])

        grupos[nome] = grupos.get(nome, 0) + valor

    grupos2 = dict(sorted(grupos.items(), key=lambda grupo:grupo[1], reverse=True))

    print("Time......................: Valor de Mercado:")
    print("--------------------------------------------:")

    for x, (valor, nome) in enumerate(grupos2.items(), start=1):
        print(f"{x:2d} {nome:30s} {valor:13d}")
        if x == 10:
            break

while True:
    titulo("Times do mundo: Exemplo de Análises")
    print("1. Top 10 Clubes + valiosos")
    print("2. Top idade + Velhos")
    print("3. Top idade + Jovens")
    print("4. Idade média dos jogadores")
    print("5. Idade por jogadores")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        topValor()
    # elif opcao == 2:
    # elif opcao == 3:
    # elif opcao == 4:
    # elif opcao == 5:
    else:
        break


# Top 10 clubes +valiosos (somar $ dos jogadores
# agrupados por clube e mostrar top 10).




# Top 10 Idade (mostrar nome, clube e idade dos 10
# +idosos e dos 10 +jovens).

# Comparar 2 clubes (ler 2 clubes e calcular a idade
# média dos jogadores de cada clube).

# Analisar por idade (ler idade, mostrar os clubes
# que têm jogadores com esta idade e quais clubes
# (do arquivo) que não têm jogadores com esta
# idade – sem repetição).