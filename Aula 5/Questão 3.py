import time 
# Leia um valor e: Mostre o valor digitado; Mostre o tipo da variável usando type()
valor = float(input("Digite um valor: "))
print("Analisando tipo...")

#programa vai passar 0.5 segundos analisando.
time.sleep(0.5)

print("Entregando resultado...")

#programa vai passar 0.2 segundos para entrega resultado.
time.sleep(0.2)

#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[0m"

#Analise do tipo de variável
print(f"O tipo de valor é",type(valor))
