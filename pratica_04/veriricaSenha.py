while True:
    try:
        senha = input("Digite sua senha: ")

        if len(senha) >= 8 and any(c.isdigit() for c in senha):
            print("Senha válida!")
            break
        else:
            print("Senha inválida.")

    except ValueError: print("Por favor digite números válidos!")