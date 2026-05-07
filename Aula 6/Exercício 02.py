positivo = 0
while True:
  numero = int(input(" Entre com um número inteiro positivo: "))
  if (numero > 0):
    positivo = positivo + 1
  else:
    print(f"Quantidade de números positivo: {positivo}")
