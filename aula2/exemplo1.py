nome = input("Nome do aluno: ")
idade = int(input('Idade: '))
salario = float(input('Salários: '))


print("\n------- Dados do Aluno -------")
print(f"Seu nome é {nome}")
print(f"Idaade: {idade} anos")
print(f"Salário R$: {salario:9.2f}")

if idade >= 40 and salario <= 5000:
  print("Acima de 40 e ganhando bem")

if nome == "Ana" or nome == "Pedro":
  print("Bonito nome")



if idade >= 18:
  print("Ah... você é maior de idade")
  bonus = 500

else:
  print("Bah... Você ainda é menor de idade")
  bonus = 300

print(f"Você recebeu um bônus de R${bonus: .2f}")
print("Bye, Bye..")
