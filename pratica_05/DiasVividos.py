from datetime import datetime

while True:
    try:
        nascimento = input("Digite sua data de nascimento (dd/mm/aaaa) (ou 0 para sair): ")

        if nascimento == '0':
            break

        dias = (datetime.now() - datetime.strptime(nascimento, "%d/%m/%Y")).days
        print(f"Você está vivo há {dias} dias.")

    except ValueError: print("Por favor digite números válidos!")