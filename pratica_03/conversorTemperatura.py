def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return None

    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9/5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return None

while True:
    try:
        valor = float(input("Digite a temperatura: "))
        origem = input("Digite a unidade de origem (C, F ou K): ").upper()
        destino = input("Digite a unidade de destino (C, F ou K): ").upper()

        resultado = converter_temperatura(valor, origem, destino)
        break
    except ValueError: print("Use Valores válidos!!")

if resultado is not None:
    print(f"{valor}°{origem} é equivalente a {resultado:.2f}°{destino}.")
else:
    print("Unidade inválida informada.")
