# def contagem_regressiva(n):
#     if n == 0:
#         print("FIM!")
    #     else:
#         print(n)
#         contagem_regressiva(n -1)

# contagem_regressiva(10)

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n -1)

print(fatorial(5))