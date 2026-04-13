idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Com {idade} anos você é menor de idade!")
elif idade <= 59:
    print(f"Com {idade} anos você é adulto!")
else:
    print(f"Com {idade} anos você é idoso!")
