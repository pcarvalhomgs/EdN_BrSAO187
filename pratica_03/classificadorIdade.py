while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade >= 0 and idade <= 12:
            print("Você é uma Criança.")
        elif idade >= 13 and idade <= 17:
            print("Você é um Adolescente.")
        elif idade >= 18 and idade <= 59:
            print("Você é um Adulto.")
        elif idade >= 60 and idade <= 110:
            print("Você é um Idoso.")
        else:
            print("Idade inválida.")
            continue
        
        break
    except ValueError: print("Use somente numeros inteiros!!")


