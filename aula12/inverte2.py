def inverte(palavra):
    if len(palavra) == 1:
        return palavra

    return palavra[-1] + inverte(palavra[0:-1])

print(inverte("ELINTON"))