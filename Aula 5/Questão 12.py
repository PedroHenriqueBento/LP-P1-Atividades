import time
# Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
numero1 = float(input("Digite seu primeiro número aqui: "))
numero2 = float(input("Digite seu segundo número aqui: "))

#Programa vai somar os numeros por 0.5 segundos.
print("Somando...")

time.sleep(0.5)

#Programa vai verificar por 0.5 segundos qual é o maior
print("Verificando qual número é maior...")

time.sleep(0.5)
soma = numero1 + numero2

if numero1 > numero2:
    print(f"A soma dos números é igual a {soma} e o número {numero1} é Maior que o número {numero2}")
elif numero2 > numero1:
    print(f"A soma dos números é igual a {soma} e o número {numero2} é Maior que o número {numero1}")
else:
    print(f"A soma dos números é igual a {soma} e o número {numero1} e {numero2} são iguais")
