while True:
    try:
        ano = int(input("Digite um ano: "))

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
        
        break
    except ValueError: print("Use um Ano Valido!!")

