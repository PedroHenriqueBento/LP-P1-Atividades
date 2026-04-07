import time 
# Leia um número e informe se ele é par ou ímpar
numero = float(input("Digite um valor: "))
print("Impar ou Par?")

#programa vai passar 1.0 segundos analisando.
time.sleep(1.0)

#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[0m"

#Decisão impar ou par
if numero % 2 == 0:
    print(f"Descobri!! O número {numero} é {green}Par!!{reset}")
else:
    print(f"Descobri!! O número {numero} é {red}Ímpar!!{reset}")
