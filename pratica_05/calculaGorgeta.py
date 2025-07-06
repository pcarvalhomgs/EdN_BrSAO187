def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
            gorjeta = valor_conta * (porcentagem_gorjeta / 100)
            return gorjeta

while True:
    try:
        valor = float(input("Digite o valor da conta: R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta: "))

        valor_gorjeta = calcular_gorjeta(valor, porcentagem)
        print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
        break

    except ValueError: print("Por favor digite números válidos!")
