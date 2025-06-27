while True:
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))

        imc = peso / (altura ** 2)

        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print(classificacao)
        break
    except ValueError: print("Use Valores válidos!!")