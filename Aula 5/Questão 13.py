import time
# Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.
numero = float(input("Digite seu número aqui: "))

print("Processando...")
#0.5 segundos processando
time.sleep(0.5)

metade = numero / 2
dobro = numero * 2 
if numero > 100:
    print(f"A metade do número {numero} é {metade}.")
else:
    print(f"O dobro do número {numero} é {dobro}.")
