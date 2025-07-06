
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    return desconto


while True:
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        percentual = float(input("Digite a porcentagem de desconto: "))

        desconto = calcular_desconto(preco, percentual)
        preco_final = preco - desconto

        print(f"\nValor do desconto: R$ {desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")

        break

    except ValueError: print("Por favor digite números válidos!")
