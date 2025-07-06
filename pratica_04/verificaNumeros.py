pares = 0
impares = 0

while True:
    numero = input("Digite um número (ou 'F' para encerrar): ")

    if numero == 'F':
        break

    if int(numero) % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
