import random

def exibir_tabuleiro(tabuleiro):
    print("\nCOL        1   2   3   4")
    print("         " + "-" * 17)
    for i in range(4):
        print(f"LIN {i+1}    |", end="")
        for j in range(4):
            if tabuleiro[i][j] == 0:
                print("   |", end="")   
            else:
                print(f"{tabuleiro[i][j]:2d} |", end="")
        print()
    print("         " + "-" * 17)


def encontrar_vazio(tabuleiro):
  for i in range(4):
    for j in range(4):
      if tabuleiro[i][j] == 0:
        return i, j


def mover_peca(tabuleiro, linha, coluna):
  li, lj = encontrar_vazio(tabuleiro)

  diff_linha = abs(linha - li)
  diff_coluna = abs(coluna - lj)

  if (diff_linha == 1 and diff_coluna == 0) or \
     (diff_linha == 0 and diff_coluna == 1):
    tabuleiro[li][lj]        = tabuleiro[linha][coluna]
    tabuleiro[linha][coluna] = 0
    return True
  else:
    return False


def embaralhar(tabuleiro):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(300):
        li, lj = encontrar_vazio(tabuleiro)
        random.shuffle(direcoes)
        for dl, dc in direcoes:
            nl, nc = li + dl, lj + dc
            if 0 <= nl < 4 and 0 <= nc < 4:
                tabuleiro[nl][nc], tabuleiro[li][lj] = \
                    tabuleiro[li][lj], tabuleiro[nl][nc]
                break


def verificar_vitoria(tabuleiro):
    esperado = list(range(1, 16)) + [0]
    atual = []
    for linha in tabuleiro:
        for val in linha:
            atual.append(val)
    return atual == esperado


def calcular_pontuacao(movimentos):
    if movimentos == 0:
        return 0
    pontuacao = max(0, 1000 - movimentos * 5)
    return pontuacao


def salvar_pontuacao(nome, pontuacao):
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome};{pontuacao}\n")


def exibir_ranking():
    try:
        with open("ranking.txt", "r") as arquivo:
            linhas = arquivo.readlines()
 
        jogadores = []
        for linha in linhas:
            partes = linha.strip().split(";")
            if len(partes) == 2:
                nome_j   = partes[0]
                pontos_j = int(partes[1])
                jogadores.append((nome_j, pontos_j))
 
        jogadores.sort(key=lambda x: x[1], reverse=True)
 
        print("\n========== RANKING ==========")
        if not jogadores:
            print("Nenhuma pontuação salva ainda.")
        else:
            for pos, (nome_j, pontos_j) in enumerate(jogadores[:10], start=1):
                print(f"  {pos}. {nome_j:<15} {pontos_j} pontos")
        print("==============================\n")
 
    except FileNotFoundError:
        print("\nNenhuma pontuação salva ainda.\n")


def jogar(nome):
    tabuleiro = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 0]
    ]
 
    print("\nEmbaralhando as peças...")
    embaralhar(tabuleiro)
 
    movimentos = 0
 
    print(f"\nBom jogo, {nome}! Coloque as peças em ordem de 1 a 15.")
    print("Digite RANKING para ver o placar ou SAIR para desistir.\n")
 
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Movimentos: {movimentos}")
 
        if verificar_vitoria(tabuleiro):
            pontuacao = calcular_pontuacao(movimentos)
            print(f"\nParabéns, {nome}! Você venceu em {movimentos} movimentos!")
            print(f"Sua pontuação: {pontuacao} pontos")
            salvar_pontuacao(nome, pontuacao)
            break
 
        entrada_linha = input("\nQual LINHA da peça que quer mover? (1-4): ").strip()
 
        if entrada_linha.upper() == "RANKING":
            exibir_ranking()
            continue
        if entrada_linha.upper() == "SAIR":
            print("Partida encerrada. Até a próxima!")
            break
 
        entrada_coluna = input("Qual COLUNA da peça que quer mover? (1-4): ").strip()
 
        if entrada_coluna.upper() == "RANKING":
            exibir_ranking()
            continue
        if entrada_coluna.upper() == "SAIR":
            print("Partida encerrada. Até a próxima!")
            break
 
        if not entrada_linha.isdigit() or not entrada_coluna.isdigit():
            print("Por favor, digite apenas números de 1 a 4.")
            continue
 
        lin = int(entrada_linha) - 1   
        col = int(entrada_coluna) - 1
 
        if not (0 <= lin < 4 and 0 <= col < 4):
            print("Posição inválida! Use valores entre 1 e 4.")
            continue
 
        if mover_peca(tabuleiro, lin, col):
            movimentos += 1
        else:
            print("Movimento inválido! A peça precisa estar ao lado do espaço vazio.")

print("=" * 40)
print("               15-PUZZLEEZ!")
print("=" * 40)
 
nome_jogador = input("Digite seu nome: ").strip()
if not nome_jogador:
    nome_jogador = "Jogador"
 

while True:
    print(f"\nOlá, {nome_jogador}!")
    print("1. Jogar")
    print("2. Ver ranking")
    print("3. Sair")
    opcao = input("Escolha uma opção: ").strip()
 
    if opcao == "1":
        jogar(nome_jogador)
    elif opcao == "2":
        exibir_ranking()
    elif opcao == "3":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")