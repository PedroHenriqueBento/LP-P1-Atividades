import time
#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.
caractere = input("Digite um número e vamos por ao quadrado: ")


#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[0m"

print("Verificando.", end="\r")
time.sleep(0.5)
print("Verificando..", end="\r")
time.sleep(0.5)
print("Verificando...", end="\r")
time.sleep(0.5)
print("Verificando   ", end="\r")
time.sleep(0.5)
print("Verificando.  ", end="\r")
time.sleep(0.5)
print("Verificando.. ", end="\r")
time.sleep(0.5)
print("Verificando...", end="\r")
time.sleep(0.5)
print("              ", end="\r")
time.sleep(0.5)

try:
    numero = float(caractere)
    tipo = type(numero)
    quadrado = numero ** 2
    print(f"O tipo de número digitado é {tipo} e o quadrado do número {caractere} é igual a {quadrado} ")
except:
    print(f"{red}Valor inválido! Você digitou uma letra.{reset}")
