# # 1 - 
# pessoas = int(input("Nº pessoas: "))
# peixes = int(input("Nº peixes: "))

# # valorEntrada = pessoas * 20.00
# # peixesExtras = max(0, peixes - pessoas)
# # valorPeixesExtras = peixesExtras * 12.00

# # valorTotal = valorEntrada + valorPeixesExtras

# # print(f"Pagar: R$ {valorTotal:.2f}")

# if peixes <= pessoas:
#   valor = pessoas * 20
# else:
#   extras = peixes - pessoas
#   valor = (pessoas * 20) + (extras * 12)

# print(f"Valor a pagar R$: {valor:.2f}")

# ----------------------

# # 2 -
# num = int(input("Número: "))

# print (f"Divisores do {num}: 1", end="")
# soma = 1

# # 5 / 2 => 2.5 e 5 // 2 => 2 (// para divisão inteira)
# for i in range (2, num // 2+1):
#   if num % i == 0:
#     print (f", {i}", end="")
#     soma = soma + i

# print()
# print(f"Soma so divisores: {soma}")

# if soma == num:
#   print(f"{num} é um número PERFEITO")
# else:
#   print(f"{num} não é um número Perfeito")
