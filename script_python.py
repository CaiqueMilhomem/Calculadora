#codigo para rodar uma calculadora que faz um calculo de apenas dois numeros (operacao binaria), com opcao de +, -, * e /

nome = input("DIgite seu nome, por favor:")
print(nome)

numero1 = int(input(f"Olá, {nome}.\nDigite o primeiro numero da conta que quer fazer: \nOBS: Essa calculadora faz a conta utilizando apenas dois numeros. \nE faz as seguintes contas: soma(+), subtracao(-), divisao(/) ou multiplicacao(*)"))
print(numero1)

numero2 = int(input(f"Olá, {nome}. Digite o segundo numero da conta que quer fazer:"))
print(numero2)

operador = input(f"{nome}, digite qual o operador que o senhor quer utilizar na conta, soma(+), subtracao(-), divisao(/) ou multiplicacao(*): \nOBS: Digite (+), (-), (/) ou (*)")
print(operador)

if operador == "+":
  print(f"{numero1} + {numero2} = {numero1 + numero2}")
elif operador == "-":
  print(f"{numero1} - {numero2} = {numero1 - numero2}")
elif operador == "/":
  print(f"{numero1} / {numero2} = {numero1 / numero2}")
elif operador == "*":
  print(f"{numero1} * {numero2} = {numero1 * numero2}")
else:
  print("Operador invalido.")
